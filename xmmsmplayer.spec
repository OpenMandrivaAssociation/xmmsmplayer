%define name xmmsmplayer
%define version 0.5
%define release %mkrel 5

Name: %{name}
Summary: An input plug-in for XMMS that plays videos using MPlayer
Version: %{version}
Release: %{release}
License: GPL
Group: Video
Source0: http://prdownloads.sourceforge.net/xmmsmplayer/%name-%{version}.tar.bz2
URL: http://www.cse.iitb.ac.in/~nandan/xmmsmplayer/
BuildRequires:	libxmms-devel
Requires: xmms
Requires: mplayer

%description
This an xmms plugin that allows you to use xmms as a front-end for
MPlayer. You'll need MPlayer properly installed and in the PATH.

%prep
%setup -q
cat /dev/null > acinclude.m4
aclocal
autoconf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%{_libdir}/xmms/Input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc ChangeLog README AUTHORS
%{_libdir}/xmms/Input/libxmmsmplayer.so


