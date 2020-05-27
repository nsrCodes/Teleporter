Use one of the following commands:

# Navigate to alias
*open directory with file explorer* 
	teleporter navigate [alias_name]	
*open a new terminal session at that particular location*
	teleporter navigate [alias_name] -t
	teleporter navigate [alias_name] --terminal

# Create an alias
	teleporter create [alias_name] [location]	

# List all current alias
	teleporter -l  //  teleporter --list	

# Delete an alias
	teleporter [delete] [alias_name]	
	
You Do can use smart type by using '.' to specify the current directory or even create aliases for subdirectories for ur current alias location in the following manner
		teleporter create [alias_name] ./subdir/anything
		teleporter create [alias_name] .									   
