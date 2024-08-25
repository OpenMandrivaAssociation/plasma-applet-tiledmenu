Name:		plasma-applet-tiledmenu
Summary:	Tiled application launcher menu, resembling Windows 10
Version:	46
Release:	1
Group:		Graphical desktop/KDE
Source0:	https://github.com/Zren/plasma-applet-tiledmenu/archive/master/%{name}-%{version}.tar.gz
Url:		https://store.kde.org/p/1160672/
License:	GPLv2+
BuildArch:	noarch

%description
Tiled application launcher menu, resembling Windows 10

%prep
%autosetup -p1 -n plasma-applet-tiledmenu-master

%build
# No building required, this is pure QML

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/
cp -a package %{buildroot}%{_datadir}/plasma/plasmoids/com.github.zren.tiledmenu

%files
%{_datadir}/plasma/plasmoids/com.github.zren.tiledmenu
