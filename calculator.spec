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
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}/
