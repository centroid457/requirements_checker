# RELEASE HISTORY

********************************************************************************
## TODO
1. add WARN_if__*/if_not__* (and use message in stderr)  
2. add check_file  

********************************************************************************
## FIXME
1. sometimes modules have incorrect SHARE!!! maybe need check upgrade after installation!!! and show ERROR!  
2. FIX TESTS!  

********************************************************************************
## NEWS

0.2.18 (2024/10/24 14:58:50)
------------------------------
- [Pkg] add check_prj_installed_latest +apply in upgrade_prj+share  

0.2.17 (2024/10/24 13:00:20)
------------------------------
- [Pkg] increase timeout for reading version  

0.2.16 (2024/10/16 14:43:59)
------------------------------
- try some fixes  

0.2.15 (2024/10/15 10:29:26)
------------------------------
- [ReqCheckVersion] zero ref  

0.2.14 (2024/09/24 14:50:44)
------------------------------
- [Version]add MIN_BLOCKS_COUNT in init  

0.2.13 (2024/09/24 14:40:11)
------------------------------
- [Version] add REQ_BLOCKS_COUNT+RAISE  

0.2.12 (2024/08/06 17:27:27)
------------------------------
- [requirements] apply last ver2  

0.2.11 (2024/08/02 10:37:50)
------------------------------
- [Pkgs] ergroup PKGSET__PyPI_DISTRIBUTION  
- [requirements] apply last ver  

0.2.10 (2024/08/01 18:20:45)
------------------------------
- [Pkgs]:  
	- fix BROKEN logic Upgrade  
	- separate PKGSET__PyPI_DISTRIBUTION  
	- add reinstall  

0.2.9 (2024/08/01 14:45:04)
------------------------------
- [Packages] try fix ensure upgrade over uninstall +add install  

0.2.8 (2024/07/29 14:07:51)
------------------------------
- [Packages.parse_files] fix prints=ljust  

0.2.7 (2024/07/29 12:04:39)
------------------------------
- [Packages] fix encoding/print + add skip_paths  

0.2.6 (2024/07/26 18:03:05)
------------------------------
- [Packages] ref parse_files__import  

0.2.5 (2024/07/24 10:57:41)
------------------------------
- [Pkgs] add parse_text/*files  

0.2.4 (2024/06/24 10:47:37)
------------------------------
- [TESTS] move into separated folder  

0.2.3 (2024/06/21 16:16:26)
------------------------------
- [CICD+BADGES] apply new ver  

0.2.2 (2024/06/19 12:08:45)
------------------------------
- [VER] apply classes_aux - finish  

0.2.1 (2024/06/19 12:05:45)
------------------------------
- [VER] apply classes_aux  

0.2.0 (2024/06/18 18:54:32)
------------------------------
- [VER] add ReqCheckVersion/Python  

0.1.16 (2024/06/17 16:53:54)
------------------------------
- [PKGS] add CmdPattern  
- [VER] del old +add VersionBlock  

0.1.15 (2024/05/30 18:28:48)
------------------------------
- [PKGSET__CENTROID_457]zero add pytest-aux  

0.1.14 (2024/05/27 15:44:37)
------------------------------
- [STR] big ref (just start):  
	- use only one check() method!  
	- renames  
	- apply variants as DICT  
	- try apply None value in params  

0.1.13 (2024/05/22 15:31:22)
------------------------------
- [__INIT__.py] fix import  
- apply last pypi template  

0.1.12 (2024/05/21 14:46:37)
------------------------------
- [Packages] add upgrade_prj  

0.1.11 (2024/05/08 12:45:42)
------------------------------
- [PKGSET__CENTROID_457]add logger-aux  

0.1.10 (2024/02/08 16:35:44)
------------------------------
- add print file content in upgrade_file  

0.1.9 (2024/02/08 16:26:35)
------------------------------
- fix upgrade_file  

0.1.8 (2024/02/06 12:16:55)
------------------------------
- add twine for share on pypi  

0.1.7 (2024/02/06 12:10:36)
------------------------------
- zero use pypi new version  

0.1.6 (2024/01/31 12:45:42)
------------------------------
- add new modules in PKGSET__CENTROID_457/2:  
	- build - as new setup  

0.1.5 (2024/01/26 17:31:01)
------------------------------
- add new modules in PKGSET__CENTROID_457:  
	- dummy-module  
	- testplans  
	- server-templates  

0.1.3 (2024/01/23 10:36:20)
------------------------------
- use current interpreter path for pkg installation  

0.1.2 (2024/01/19 16:34:41)
------------------------------
- add with tests:  
	- version_get_installed  
	- check_installed  
	- uninstall  

0.1.1 (2024/01/18 12:18:30)
------------------------------
- show result for module installation  
- apply new PRJ version 0.0.2  

0.1.0 (2024/01/14 07:58:12)
------------------------------
- apply new pypi template  

0.0.9 (2024-01-14)
-------------------
- move requirents__centr457 from file into list + add all projects

0.0.8 (2024-01-14)
-------------------
- fix ReqCheckStr_Os for derivatives without settings
- try add Packages as modules upgrades

0.0.7 (2023-12-18)
-------------------
- rename getattr from check_is__/check_is_not__ into bool_if/raise_if/not

0.0.6 (2023-12-07)
-------------------
- apply check_is__/check_is_not__/+getattr as classmethod and instancemethod

0.0.5 (2023-12-06)
-------------------
- add settings in __init__

0.0.4 (2023-12-06)
-------------------
- deprecate samples in check()

0.0.3 (2023-12-06)
-------------------
- add check_is__/check_is_not__/+getattr
- add setting _MEET_TRUE

0.0.2 (2023-12-04)
-------------------
- add ReqCheckStr_Os
- add ReqCheckStr_Arch

0.0.1 (2023-12-01)
-------------------
- first variant

********************************************************************************
