%define git 0

Name: lxqt-runner
Version: 0.9.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 5
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: lxqt-runner-0.9.0-run-new-process-as-a-direct-child.patch
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
%{_datadir}/lxqt/lxqt-runner
