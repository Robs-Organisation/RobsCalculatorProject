Name:           RobsCalculatorProject
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/%{name}
Source0:        %{name}-%{version}.tar.gz

Requires:       postgresql

%description
This is a description

%prep
%setup -c

%post
sed -i "s/SESSION_SECRET=""/\SESSION_SECRET="$(openssl rand -hex 30)"/" %{_sysconfdir}/%{name}/override.conf

%files
%license LICENSE
%{_bindir}/%{name}/

%config(noreplace)
%{_sysconfdir}/%{name}/*

%clean
rm -rf $%{_builddir}
rm -rf %{buildroot}/%{_bindir}/%{name}
rm -rf %{buildroot}/%{_sysconfdir}/%{name}
rm -rf %{buildroot}/lib/systemd/system/
rm -rf $%{buildroot}/%{_datadir}/%{name}/
