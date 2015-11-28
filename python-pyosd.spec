
%define		module	pyosd

Summary:	xosd bindings for Python
Summary(pl.UTF-8):	Moduł xosd dla Pythona
Name:		python-%{module}
Version:	0.2.14
Release:	3
License:	GNU
Group:		Development/Languages/Python
Source0:	http://repose.cx/pyosd/%{module}-%{version}.tar.gz
# Source0-md5:	3beb6692c4d76b3318e7876a6dd03bdf
URL:		http://repose.cx/pyosd/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	xosd-devel >= 2.2.5
Requires:	xosd >= 2.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyosd is a Python module for displaying text on your X display, much
like the "On Screen Displays" used on TVs and some monitors.

This is useful for such things as displaying the currently playing
song in your media player.

%description -l pl.UTF-8
pyosd jest modułem dla języka Python umożliwiającym wyświetlanie
tekstów na ekranie serwera X, podobnie jak "On Screen Display" używany
w telewizorach i monitorach.

Może to zostać wykorzystane do wyświetlania aktualnie odtwarzanej
piosenki czy filmu.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%py_install \
	--install-lib=%{py_sitedir} \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ChangeLog pyosd.html
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
