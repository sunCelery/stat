NAME=$(cat name)
PWD=$(pwd)

daemon-update:
	@ /usr/bin/source .venv/bin/activate && \
	python bake_stat_fetching_daemon.py && \
	python bake_stat_fetching_timer.py && \
	/usr/bin/cp -fu $PWD/systemd/* /usr/lib/systemd/system && \
	/usr/bin/systemctl daemon-reload && \
	/usr/bin/systemctl enable --now $NAME.service $NAME.timer && \
	/usr/bin/systemctl restart $NAME.service $NAME.timer

