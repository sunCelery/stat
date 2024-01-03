from configparser import ConfigParser
from pathlib import Path

from config import settings


class SystemdServiceBaker:
    def __init__(self):
        self.systemd_service_name = f'{settings.NAME}.service'
        self.systemd_services_dir = Path(
            settings.BASE_DIR,
            settings.SYSTEMD_DIR,
        )
        self.systemd_service_path = Path(
            self.systemd_services_dir,
            self.systemd_service_name,
        )
        self.systemd_services_dir.mkdir(parents=True, exist_ok=True)
        self.systemd_service_path.touch()

    def bake(self) -> None:
        config = self.bake_systemd_service()
        with open(self.systemd_service_path, 'w') as f:
            config.write(f)

    def bake_systemd_service(self) -> ConfigParser:
        config = self._read_config()
        config['Unit'] = {
            'Description': f'{settings.NAME} (daemon that gathering github statistics)',
            'After': 'multi-user.target',
        }
        config['Service'] = {
            'Restart': 'always',
            'WorkingDirectory': settings.BASE_DIR,
            'ExecStart':
                f"/usr/bin/sh -c '/usr/bin/source .venv/bin/activate && python daemon.py'",
        }
        config['Install'] = {'WantedBy': 'multi-user.target'}
        return config

    def _read_config(self) -> ConfigParser:
        config = ConfigParser(allow_no_value=True, interpolation=None)
        config.optionxform = str
        config.read(self.systemd_service_path)
        return config


if __name__ == '__main__':
    SystemdServiceBaker().bake()
