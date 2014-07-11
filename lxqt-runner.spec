Name: lxqt-runner
Version: 0.7.0
Release: 3
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: Launcher runner for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt_globalkeys)
BuildRequires: cmake(lxqt_globalkeys_ui)
BuildRequires: qt4-devel

%description
Launcher runner for the LXQt desktop

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/lxqt-runner
%{_datadir}/lxqt/lxqt-runner
