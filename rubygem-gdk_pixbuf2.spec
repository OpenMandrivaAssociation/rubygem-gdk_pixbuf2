%define  _empty_manifest_terminate_build 0
Summary:	Ruby binding of GdkPixbuf-2.x
Name:		rubygem-gdk_pixbuf2
Version:	3.4.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/gdk_pixbuf2-%{version}.gem
BuildRequires:	ruby-devel
BuildRequires:  rubygem-pkg-config
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  rubygem-native-package-installer
BuildRequires:	rubygem-rake

Obsoletes:      ruby-gdkpixbuf2

%description
Ruby binding of GdkPixbuf-2.x.

%prep
%autosetup -p1 -n  %{gem_name}-%{version}

%build
%gem_build 

%install
%gem_install

%files
%{gem_files}
