Summary:	CUDA template library
Name:		cudatemplates
Version:	0.2.2
Release:	1
License:	GPL v3 or later
Group:		Development/Libraries
Source:		%{name}-%{version}.tar.bz2
Vendor:		Institute for Computer Graphics and Vision, Graz University of Technology, Austria
URL:		http://www.icg.tugraz.at
Packager:	Institute for Computer Graphics and Vision, Graz University of Technology, Austria
Prefix:		%{_prefix}
BuildRoot: 	%{_tmppath}/buildroot-%{name}-%{version}
BuildArch: 	noarch
Requires: 	boost
BuildRequires: 	cmake boost-devel doxygen graphviz

#%define build_type Debug
%define build_type MinSizeRel

%description
...

%prep
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%setup

%build
cmake \
-DCMAKE_BUILD_TYPE:STRING=%{build_type} \
-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
.
#make doc
mkdir -p doc/html

%install
DESTDIR=$RPM_BUILD_ROOT make install
find -type f -exec chmod ugo-w {} \;

%clean
make clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/html
%doc LICENSE
%{_includedir}/%{name}
%{_datadir}/CudaTemplates
