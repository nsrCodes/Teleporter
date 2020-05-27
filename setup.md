YOU can try the file as a regular python file or even make it a permanent shell command like I have.

1. First clone this repo using 
	git clone

2. Then go to your home directory and create the ~/bin directory
	$ mkdir -p ~/bin

3. Copy all the contents of this repo into this directory via terminal using the cp command

4. Open the .bashrc file using your favourite text editor and export the path to this bin folder inside it (Don't want to be technical, follow the steps below)
	open the terminal in home directory
	$ nano  .bashrc
	copy the following command at the end of this file
	 export PATH=$PATH":$HOME/bin"
	save the file with ctrl+O and exit editor with ctrl+x

And that is it. Now even you can teleport across your directories with a simple command