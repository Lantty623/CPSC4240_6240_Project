BIN_DIR := ~/bin

.PHONY: all create_bin_dir

all: create_bin_dir
	@echo "Creating directories..."
	@mkdir -p ~/.local/share/nautilus/commands
	@mkdir -p ~/.local/share/nautilus/scripts
	@echo "Copying files to scripts directory..."
	@cp -r  $(CURDIR)/Scripts/* ~/.local/share/nautilus/scripts
	@cp -r  $(CURDIR)/securefolder/securefolder.py ~/.local/share/nautilus/commands
	@echo "Adding scripts to ~/.bashrc"
	@python3 $(CURDIR)/securefolder/addAlias.py
	@echo "Setting permissions..."
	@chmod +x ~/.local/share/nautilus/commands/securefolder.py
	@chmod +x ~/.local/share/nautilus/scripts/PasswordSafe
	@chmod +x ~/.local/share/nautilus/scripts/SafeEncrypt
	@chmod 744 $(CURDIR)/securefolder/securefolder.py
	@chmod 744 $(CURDIR)/securefolder/hashtest.py
	@echo "moving securefolder and hashtest to ~/bin"
	@cp $(CURDIR)/securefolder/securefolder.py ~/bin/securefolder
	@cp $(CURDIR)/securefolder/hashtest.py ~/bin/hashtest
	@echo "gui reset..."
	@nautilus -q &
	@nohup nautilus -q > /dev/null 2>&1 &
	@sleep 2
	@echo "updating bashrc file"
	@. ~/.bashrc
	@echo "*** everything is setup and good to go! ***"

FolderSafe:
	~/.local/share/nautilus/scripts/PasswordSafe

create_bin_dir:
	@if [ ! -d $(BIN_DIR) ]; then \
		echo "Creating a /bin directory in home"; \
		mkdir $(BIN_DIR); \
	else \
		echo "$(BIN_DIR) already exists"; \
	fi