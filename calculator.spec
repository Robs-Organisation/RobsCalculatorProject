Name:           CalcBuffaloBinary
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        CalcBuffaloBinary

Requires:       postgresql

%description
This is a description

%prep
%setup -q

%install
%make_install


%files
%{_bindir}/%{name}
