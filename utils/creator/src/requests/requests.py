import os 

class Requests:
    def __init__(self): 
        pass
        
    def get_server(self):
        return os.environ.get("__SERVER__")

    def get_allusersprofile(self):
        return self.SERVER["ALLUSERSPROFILE"]

    def get_appdata(self):
        return self.SERVER["APPDATA"]

    def get_chrome_crashpad_pipe_name(self):
        return self.SERVER["CHROME_CRASHPAD_PIPE_NAME"]

    def get_commonprogramfiles(self):
        return self.SERVER["COMMONPROGRAMFILES"]

    def get_commonprogramfiles_x86(self):
        return self.SERVER["COMMONPROGRAMFILES(X86)"]

    def get_commonprogramw6432(self):
        return self.SERVER["COMMONPROGRAMW6432"]

    def get_computername(self):
        return self.SERVER["COMPUTERNAME"]

    def get_comspec(self):
        return self.SERVER["COMSPEC"]

    def get_driverdata(self):
        return self.SERVER["DRIVERDATA"]

    def get_fps_browser_app_profile_string(self):
        return self.SERVER["FPS_BROWSER_APP_PROFILE_STRING"]

    def get_fps_browser_user_profile_string(self):
        return self.SERVER["FPS_BROWSER_USER_PROFILE_STRING"]

    def get_homedrive(self):
        return self.SERVER["HOMEDRIVE"]

    def get_homepath(self):
        return self.SERVER["HOMEPATH"]

    def get_localappdata(self):
        return self.SERVER["LOCALAPPDATA"]

    def get_logonserver(self):
        return self.SERVER["LOGONSERVER"]

    def get_number_of_processors(self):
        return self.SERVER["NUMBER_OF_PROCESSORS"]

    def get_onedrive(self):
        return self.SERVER["ONEDRIVE"]

    def get_onedriveconsumer(self):
        return self.SERVER["ONEDRIVECONSUMER"]

    def get_original_xdg_current_desktop(self):
        return self.SERVER["ORIGINAL_XDG_CURRENT_DESKTOP"]

    def get_os(self):
        return self.SERVER["OS"]

    def get_path(self):
        return self.SERVER["PATH"]

    def get_pathext(self):
        return self.SERVER["PATHEXT"]

    def get_processor_architecture(self):
        return self.SERVER["PROCESSOR_ARCHITECTURE"]

    def get_processor_identifier(self):
        return self.SERVER["PROCESSOR_IDENTIFIER"]

    def get_processor_level(self):
        return self.SERVER["PROCESSOR_LEVEL"]

    def get_processor_revision(self):
        return self.SERVER["PROCESSOR_REVISION"]

    def get_programdata(self):
        return self.SERVER["PROGRAMDATA"]

    def get_programfiles(self):
        return self.SERVER["PROGRAMFILES"]

    def get_programfiles_x86(self):
        return self.SERVER["PROGRAMFILES(X86)"]

    def get_programw6432(self):
        return self.SERVER["PROGRAMW6432"]

    def get_psmodulepath(self):
        return self.SERVER["PSMODULEPATH"]

    def get_public(self):
        return self.SERVER["PUBLIC"]

    def get_sessionname(self):
        return self.SERVER["SESSIONNAME"]

    def get_systemdrive(self):
        return self.SERVER["SYSTEMDRIVE"]

    def get_systemroot(self):
        return self.SERVER["SYSTEMROOT"]

    def get_temp(self):
        return self.SERVER["TEMP"]

    def get_tmp(self):
        return self.SERVER["TMP"]

    def get_userdomain(self):
        return self.SERVER["USERDOMAIN"]

    def get_userdomain_roamingprofile(self):
        return self.SERVER["USERDOMAIN_ROAMINGPROFILE"]

    def get_username(self):
        return self.SERVER["USERNAME"]

    def get_userprofile(self):
        return self.SERVER["USERPROFILE"]

    def get_vbox_msi_install_path(self):
        return self.SERVER["VBOX_MSI_INSTALL_PATH"]

    def get_windir(self):
        return self.SERVER["WINDIR"]

    def get_term_program(self):
        return self.SERVER["TERM_PROGRAM"]

    def get_term_program_version(self):
        return self.SERVER["TERM_PROGRAM_VERSION"]

    def get_lang(self):
        return self.SERVER["LANG"]

    def get_colorterm(self):
        return self.SERVER["COLORTERM"]

    def get_vscode_injection(self):
        return self.SERVER["VSCODE_INJECTION"]
