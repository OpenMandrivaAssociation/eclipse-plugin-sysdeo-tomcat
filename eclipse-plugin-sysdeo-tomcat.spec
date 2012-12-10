%define	oname	eclipse
%define	plugin	sysdeo-tomcat
%define	name	%{oname}-plugin-%{plugin}
%define	version	3.1.0
%define	release	3

Name:		%{name}
Summary:	Sysdeo Eclipse Tomcat Launcher plugin
Version:	%{version}
Release:	%mkrel %{release}
License:	MIT
Url:		http://www.sysdeo.com/eclipse/tomcatplugin/
Group:		Development/Java
Source0:	http://www.sysdeo.com/sysdeo/content/download/393/4930/file/tomcatPluginV31.zip
BuildArch:	noarch
Requires:	eclipse tomcat5-webapps
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Plugin for Eclipse that helps out creating Tomcat projects.

Plugin features:
* Starting, stopping and restarting Tomcat 4.x, 5.x, 3.3 
* Registering Tomcat process to Eclipse debugger 
* Creating a WAR project (wizard can update server.xml file) 
* Adding Java Projects to Tomcat classpath 
* Setting Tomcat JVM parameters, classpath and bootclasspath 
* Exporting a Tomcat project to a WAR File 
* Choosing Tomcat configuration file 
* Capability to use a special Tomcat classloader to have classes
  in several java projects loaded at the same classloader level
  than classes in a Tomcat project, see readmeDevLoader.html

%prep
%setup -q -c -T -a0

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/eclipse/plugins
cp -r com.sysdeo.eclipse.tomcat_%{version} %{buildroot}%{_datadir}/eclipse/plugins

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/eclipse/plugins/com.sysdeo.eclipse.tomcat_%{version}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-3mdv2011.0
+ Revision: 618002
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.1.0-2mdv2010.0
+ Revision: 428506
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.1.0-1mdv2008.1
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 3.1.0-1mdv2007.0
- initial release

