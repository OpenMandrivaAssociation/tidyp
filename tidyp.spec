%define libname %mklibname %{name} 1.04
%define develname %mklibname %name -d

Summary:	Program for tidying up messy HTML
Name:		tidyp
Version:	1.04
Release:	5
Group:		Text tools
License:	W3C License
URL:		http://tidyp.com/
Source0:	http://github.com/downloads/petdance/tidyp/tidyp-%{version}.tar.gz
Patch0:		tidy-20081224cvs-fix-format-errors.patch

%description
tidyp is a program that can validate your HTML, as well as modify it to be more
clean and standard. tidyp does not validate HTML 5.

libtidyp is the library on which the program is based. It can be used by any
other program that can interface to it. The Perl module HTML::Tidy is based on
this library, allowing Perl programmers to easily validate HTML.

tidyp is a fork of the tidy project.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2011.0
+ Revision: 603003
- import tidyp

