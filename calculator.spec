Name:           CalcBuffalo
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

%files
%{_datadir}/*
