%include	/usr/lib/rpm/macros.python

%define         module	pyosd

Summary:	xosd bindings for Python
Summary(pl):	Modu� xosd dla Pythona
Name:		python-%{module}
Version:	0.2.9
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://repose.cx/pyosd/%{module}-%{version}.tar.gz
# Source0-md5:	a5f0dbdd7516518a82538f20e1266fb9
URL:		http://repose.cx/pyosd/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyosd is a Python module for displaying text on your X display, much
like the "On Screen Displays" used on TVs and some monitors.

This is useful for such things as displaying the currently playing
song in your media player.

%description -l pl
pyosd jest modu�em dla j�zyka Python umo�liwiaj�cym wy�wietlanie
tekst�w na ekranie serwera X, podobnie jak "On Screen Display" u�ywany
w telewizorach i monitorach.

Mo�e to zosta� wykorzystane do wy�wietlania aktualnie odtwarzanej
piosenki czy filmu.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ChangeLog pyosd.html
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/*.so
