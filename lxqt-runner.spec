Name: lxqt-runner
Version: 1.4.0
Release: %{?git:1.%git.}1
Source0: https://github.com/lxqt/lxqt-runner/releases/download/%{version}/lxqt-runner-%{version}.tar.xz
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/Other
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-globalkeys)
BuildRequires: cmake(lxqt-globalkeys-ui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(lxqt-build-tools)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(muparser)

%description
Launcher runner for the LXQt desktop.

%prep
%autosetup -p1
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/lxqt-runner
%{_sysconfdir}/xdg/autostart/lxqt-runner.desktop
%{_mandir}/man1/*
%dir %{_datadir}/lxqt/translations/lxqt-runner
