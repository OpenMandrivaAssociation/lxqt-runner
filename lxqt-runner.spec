%define git 0

Name: lxqt-runner
Version: 0.14.1
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
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
%if %git
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1
%endif
%apply_patches
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
