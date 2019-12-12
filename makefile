install:
	@chmod +x $$(pwd)/ssh-mount.py
	@chmod +x $$(pwd)/ssh-unmount.py

	@ln -s $$(pwd)/config.json $$HOME/.config/sshmounter.json
	@ln -s $$(pwd)/ssh-mount.py /usr/bin/ssh-mount
	@ln -s $$(pwd)/ssh-unmount.py /usr/bin/ssh-unmount

uninstall:
	@rm -rf $$HOME/.config/sshmounter.json
	@rm -rf /usr/bin/ssh-mount
	@rm -rf /usr/bin/ssh-unmount