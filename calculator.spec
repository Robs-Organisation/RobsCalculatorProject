Name:           CalcBuffaloBinary
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        https://github.com/Robs-Organisation/RobsCalculatorProject/%{name}/%{name}-%{version}.tar.gz

Requires:       postgresql

%description
This is a description

%prep

%setup -q

%install

%files
/home/rpmbuild/%{name}
