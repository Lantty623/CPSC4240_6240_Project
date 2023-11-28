BIN_DIR := ~/bin

.PHONY: all create_bin_dir gui

all: create_bin_dir
	@echo "Adding scripts to ~/.bashrc"
	@python3 $(CURDIR)/securefolder/addAlias.py
	@echo "Setting permissions..."
	@chmod 744 $(CURDIR)/securefolder/securefolder.py
	@chmod 744 $(CURDIR)/securefolder/hashtest.py
	@chmod 744 $(CURDIR)/Crypto/main.py
	@echo "moving securefolder and hashtest to ~/bin"
	@cp $(CURDIR)/securefolder/securefolder.py ~/bin/securefolder
	@cp $(CURDIR)/securefolder/hashtest.py ~/bin/hashtest
	@echo "updating bashrc file"
	@. ~/.bashrc
	@echo "*** everything is setup and good to go! ***"

create_bin_dir:
	@if [ ! -d $(BIN_DIR) ]; then \
		echo "Creating a /bin directory in home"; \
		mkdir $(BIN_DIR); \
	else \
		echo "$(BIN_DIR) already exists"; \
	fi

gui:
	@echo "Creating directories..."
	@mkdir -p ~/.local/share/nautilus/commands
	@mkdir -p ~/.local/share/nautilus/scripts
	@echo "Copying files to scripts directory..."
	@cp -r  $(CURDIR)/Scripts/* ~/.local/share/nautilus/scripts
	@cp -r  $(CURDIR)/securefolder/securefolder.py ~/.local/share/nautilus/commands
	@rsync -av --exclude="__pycache__" --exclude="README.md" "$(CURDIR)/Crypto/" ~/.local/share/nautilus/commands/
	@echo "Setting permissions..."
	@chmod +x ~/.local/share/nautilus/commands/securefolder.py
	@chmod +x ~/.local/share/nautilus/commands/main.py
	@chmod +x ~/.local/share/nautilus/commands/key_management.py
	@chmod +x ~/.local/share/nautilus/commands/file_processor.py
	@chmod +x ~/.local/share/nautilus/commands/crypto_utils.py
	@chmod +x ~/.local/share/nautilus/scripts/Decrypt
	@chmod +x ~/.local/share/nautilus/scripts/Encrypt
	@chmod +x ~/.local/share/nautilus/scripts/FolderSecure
	@chmod +x ~/.local/share/nautilus/scripts/FolderSecure_Encrypt
	@chmod +x ~/.local/share/nautilus/scripts/FolderUnlock
	@chmod +x ~/.local/share/nautilus/scripts/FolderUnlock_Decrypt
	@echo "gui reset..."
	@nautilus -q &
	@nohup nautilus -q > /dev/null 2>&1 &
	@sleep 2
	@echo "*** gui is setup and ready to go! ***"
