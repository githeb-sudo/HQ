from framework.main import FutMainClass
import framework.tools.logger
from framework.lib.fut_allure import FutAllureClass
from .globals import FUT_MAIN_GLOBAL
import pytest,subprocess,shlex
global log
if 'log' not in globals():
    log = framework.tools.logger.get_logger()

order_exec = 0


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="main_init", scope="session")
def test_main_init():
    log.info('Initializing FUTMain class')
    pytest.dut_handler = pytest.ref_handler = pytest.client_handler = None
    pytest.fut_main = FutMainClass()
    log.info('FUTMain class initialized')


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="dut_init", scope="session", depends=["main_init"])
def test_dut_init():
    log.info('Acquiring dut device API')
    dut_api = pytest.fut_main.get_pod_api('dut')
    dut_handler = pytest.fut_main.get_test_handler(dut_api)
    pytest.dut_handler = dut_handler
    log.info('Device dut initialized')

# @pytest.mark.skip(reason="No ref devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="ref_init", scope="session", depends=["main_init"])
# def test_ref_init():
#     log.info('Acquiring ref device API')
#     ref_api = pytest.fut_main.get_pod_api('ref')
#     ref_handler = pytest.fut_main.get_test_handler(ref_api)
#     pytest.ref_handler = ref_handler
#     log.info('Device ref initialized')

# @pytest.mark.skip(reason="No client devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="client_init", scope="session", depends=["main_init"])
# def test_client_init():
#     log.info('Acquiring client device API')
#     client_api = pytest.fut_main.get_pod_api('client')
#     client_handler = pytest.fut_main.get_test_handler(client_api)
#     pytest.client_handler = client_handler
#     log.info('Device client initialized')


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="fut_release_version", scope="session", depends=["main_init"])
def test_fut_release_version(pytestconfig):
    version = pytest.fut_main.get_fut_release_version()
    fut_release_version = version[0].strip()
    allure_dir_option = pytestconfig.getoption('allure_report_dir')
    if allure_dir_option:
        f_allure = FutAllureClass(allure_dir_option)
        f_allure.set_release_version(fut_release_version)


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="server_device_version", scope="session", depends=["main_init"])
def test_server_device_version(pytestconfig):

    #version = pytest.fut_main.get_server_device_version()
    #server_device_version = version[0].strip()
    #version_split = server_device_version.split(' ')[0]

    get_version_cmd="uname -r"
    output=(str((subprocess.Popen(shlex.split(get_version_cmd), stdout=subprocess.PIPE)).communicate()))
    version_split=output[output.find("\'")+1:output.find("\\")]
    allure_dir_option = pytestconfig.getoption('allure_report_dir')
    if allure_dir_option:
        f_allure = FutAllureClass(allure_dir_option)
        f_allure.set_server_version(version_split)


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="dut_device_version", scope="session", depends=["dut_init"])
def test_dut_device_version(pytestconfig, is_transfer_only):
    if is_transfer_only:
        pytest.skip('Transfer only, test not required')
    model = pytest.dut_handler.shell_cfg.get('MODEL')
    version = pytest.dut_handler.get_version()
    allure_dir_option = pytestconfig.getoption('allure_report_dir')
    if allure_dir_option:
        f_allure = FutAllureClass(allure_dir_option)
        f_allure.set_device_version('dut', model, version)

# @pytest.mark.skip(reason="No ref devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="ref_device_version", scope="session", depends=["ref_init"])
# def test_ref_device_version(pytestconfig, is_transfer_only):
#     if is_transfer_only:
#         pytest.skip('Transfer only, test not required')
#     model = pytest.ref_handler.shell_cfg.get('MODEL')
#     version = pytest.ref_handler.get_version()
#     allure_dir_option = pytestconfig.getoption('allure_report_dir')
#     if allure_dir_option:
#         f_allure = FutAllureClass(allure_dir_option)
#         f_allure.set_device_version('ref', model, version)

# @pytest.mark.skip(reason="No client devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="client_device_version", scope="session", depends=["client_init"])
# def test_client_device_version(pytestconfig, is_transfer_only):
#     if is_transfer_only:
#         pytest.skip('Transfer only, test not required')
#     model = pytest.client_handler.shell_cfg.get('MODEL')
#     version = pytest.client_handler.get_version()
#     allure_dir_option = pytestconfig.getoption('allure_report_dir')
#     if allure_dir_option:
#         f_allure = FutAllureClass(allure_dir_option)
#         f_allure.set_device_version('client', model, version)


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="dut_tmp_mount_executable", scope="session", depends=["dut_init"])
def test_dut_tmp_mount_executable():
    log.info('Testing DUT tmpfs mount permission')
    fut_top_dir = pytest.dut_handler.shell_cfg.get('FUT_TOPDIR')
    fut_top_dir_mount_point = fut_top_dir.split('/')[1]
    if not fut_top_dir_mount_point:
        log.error(f'Incorrect FUT_TOPDIR path: FUT_TOPDIR=="{fut_top_dir}"')
        assert False
    perm_check_cmd = f"mount && mount | grep -q 'on /{fut_top_dir_mount_point} ' | grep -q 'noexec'"
    log.info(f'Executing on (dut): {perm_check_cmd}')
    res = pytest.dut_handler.pod_api.run_raw(perm_check_cmd)
    print(res[1])
    assert res[0] == 1


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(name="dut_transfer", scope="session", depends=["dut_init"])
def test_dut_transfer(is_transfer_only):
    log.info('Testing FUT transfer to dut')
    assert pytest.dut_handler.transfer(full=is_transfer_only)
    assert pytest.dut_handler.create_and_transfer_fut_set_env()

# @pytest.mark.skip(reason="No ref devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="ref_transfer", scope="session", depends=["ref_init"])
# def test_ref_transfer(is_transfer_only):
#     log.info('Testing FUT transfer to ref')
#     assert pytest.ref_handler.transfer(full=is_transfer_only)
#     assert pytest.ref_handler.create_and_transfer_fut_set_env()

# @pytest.mark.skip(reason="No ref devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="client_transfer", scope="session", depends=["client_init"])
# def test_client_transfer(is_transfer_only):
#     log.info('Testing FUT transfer to client')
#     assert pytest.client_handler.transfer(full=is_transfer_only)
#     assert pytest.client_handler.create_and_transfer_fut_set_env()


@pytest.mark.run(order=order_exec+1)
@pytest.mark.dependency(
    name="dut_ready", scope="session", depends=["dut_init", "dut_transfer", "dut_tmp_mount_executable"]
)
def test_dut_ready():
    pytest.dut_handler.is_ready = True
    pytest.fut_main.test_device_handlers.append(pytest.dut_handler)
    FUT_MAIN_GLOBAL.test_device_handlers.append(pytest.dut_handler)
    assert True

# @pytest.mark.skip(reason="No ref devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="ref_ready", scope="session", depends=["ref_init", "ref_transfer"])
# def test_ref_ready():
#     pytest.ref_handler.is_ready = True
#     pytest.fut_main.test_device_handlers.append(pytest.ref_handler)
#     FUT_MAIN_GLOBAL.test_device_handlers.append(pytest.ref_handler)
#     assert True

# @pytest.mark.skip(reason="No client devices")
# @pytest.mark.run(order=order_exec+1)
# @pytest.mark.dependency(name="client_ready", scope="session", depends=["client_init", "client_transfer"])
# def test_client_ready():
#     pytest.client_handler.is_ready = True
#     pytest.fut_main.test_device_handlers.append(pytest.client_handler)
#     FUT_MAIN_GLOBAL.test_device_handlers.append(pytest.client_handler)
#     assert True


@pytest.mark.run(order=order_exec+1)
def test_is_transfer_only(is_transfer_only):
    if is_transfer_only:
        pytest.exit('Transfer only - quiting')
    else:
        pytest.skip('Continuing...')
