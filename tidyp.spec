%define name	tidyp
%define version 1.04
%define release %mkrel 1
%define libname %mklibname %{name} 1.04
%define develname %mklibname %name -d

Summary:	Program for tidying up messy HTML
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Text tools
License:	W3C License
URL:		http://tidyp.com/
Source0:	http://github.com/downloads/petdance/tidyp/tidyp-%{version}.tar.gz
Patch0:		tidy-20081224cvs-fix-format-errors.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so

