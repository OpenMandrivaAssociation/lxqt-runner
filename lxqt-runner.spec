%define git 0

Name: lxqt-runner
Version: 0.10.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 2
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-globalkeys)
BuildRequires: cmake(lxqt-globalkeys-ui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(libmenu-cache)

%description
Launcher runner for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches
%cmake_qt5

%build
%make -C build

%install
%makeinstall_std -C build

%find_lang %{name} --with-qt

%files -f %{name}.lang
%{_bindir}/lxqt-runner
