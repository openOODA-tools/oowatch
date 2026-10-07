Name:           oowatch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Continuous command scheduler and delta watcher with ANSI diff highlighting
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oowatch
Source0:        oowatch-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oowatch is a sovereign continuous command scheduler and delta watcher written
in pure openOODA, featuring periodic execution, ANSI delta line diff highlighting
via oote themes, execution count bounds, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oowatch
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oowatch-uninstall

%files
/usr/bin/oowatch
/usr/bin/oowatch-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign release: continuous delta watcher, diff highlighting, and MCP stdio surface
