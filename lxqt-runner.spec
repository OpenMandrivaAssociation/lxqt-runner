%define git 0

Name: lxqt-runner
Version: 0.8.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 2
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt-qt5)
BuildRequires: cmake(lxqt-globalkeys-qt5)
BuildRequires: cmake(lxqt-globalkeys-ui-qt5)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: qt5-devel

%description
Launcher runner for the LXQt desktop

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/lxqt-runner
%{_datadir}/lxqt-qt5/translations/lxqt-runner
%{_datadir}/lxqt/lxqt-runner
