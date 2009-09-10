Name:		task-wm5sync-gnome
Version:	1.0
Release:	%{mkrel 2}
Summary:	GNOME metapackage for connecting to Windows Mobile 5+
Group:		Communications
License:	GPLv2+
Requires:	task-wm5sync-common
Requires:	libopensync-plugin-evolution2
Suggests:	synce-kpm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with GNOME applications. At present it also suggests the
synce-kpm package, even though this is a Qt-based application, as it is
clearly the best available application for graphically configuring
partnerships and installing / removing software on these devices.

%files

