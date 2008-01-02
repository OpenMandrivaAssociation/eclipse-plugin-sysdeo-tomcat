%define	oname	eclipse
%define	plugin	sysdeo-tomcat
%define	name	%{oname}-plugin-%{plugin}
%define	version	3.1.0
%define	release	1

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

