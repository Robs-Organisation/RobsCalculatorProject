Name:           calculator
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        %{name}-%{version}.tar.gz

Requires:       postgresql

%description
This is a description

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}/
