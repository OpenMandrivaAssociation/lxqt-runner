%define git 0

Name: lxqt-runner
Version: 0.11.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/Other
# (tpg) patches from upstream git
Patch0: 0000-Fix-endif-placement-when-test-for-MATH-library.patch
Patch1: 0001-Remove-cpack-49.patch
Patch2: 0002-Fixes-FTBFS-when-libmenu-cache-was-installed-to-non-.patch
Patch3: 0003-Use-the-new-MenuCache-configuration-CMake-module.patch
Patch4: 0004-MathItem-Honor-system-locale-52.patch
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
BuildRequires: cmake(lxqt-build-tools)
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
