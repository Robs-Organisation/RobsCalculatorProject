Name:           calculator
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        calculator-1.0.tar.gz

Requires:       postgresql

%description
This is a description

%prep
%setup -q

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin

%files
%{_bindir}/%{name}/