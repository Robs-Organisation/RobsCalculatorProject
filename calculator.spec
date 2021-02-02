Name:           CalcBuffaloBinary
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        CalcBuffaloBinary-1.0.tar.gz

Requires:       postgresql

%description
This is a description

%prep

%setup

%build
make 

%install 
install -m 0755 -d %{buildroot}/%{_datadir}/
cp -a data/* %{buildroot}/%{_datadir}/

%files
%{_datadir}/CalcBuffaloBinary
