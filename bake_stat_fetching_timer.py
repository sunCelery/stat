from configparser import ConfigParser
from pathlib import Path

import settings


class SystemdTimerBaker:
    def __init__(self):
        self.systemd_timer_name = f'{settings.NAME}.timer'
        self.systemd_services_dir = Path(
            settings.BASE_DIR,
            settings.SYSTEMD_DIR,
        )
        self.systemd_timer_path = Path(
            self.systemd_services_dir,
            self.systemd_timer_name,
        )
        self.systemd_services_dir.mkdir(parents=True, exist_ok=True)
        self.systemd_timer_path.touch()

    def bake(self) -> None:
        config = self.bake_systemd_timer()
        with open(self.systemd_timer_path, 'w') as f:
            config.write(f)

    def bake_systemd_timer(self) -> ConfigParser:
        config = self._read_config()
        config['Unit'] = {
            'Description': f'Scheduler for {settings.NAME}.service',
        }
        config['Timer'] = {
            'OnCalendar': 'daily',
            'Persistent': True,
        }
        config['Install'] = {'WantedBy': 'timers.target'}
        return config

    def _read_config(self) -> ConfigParser:
        config = ConfigParser(allow_no_value=True, interpolation=None)
        config.optionxform = str
        config.read(self.systemd_timer_path)
        return config


if __name__ == '__main__':
    SystemdTimerBaker().bake()
