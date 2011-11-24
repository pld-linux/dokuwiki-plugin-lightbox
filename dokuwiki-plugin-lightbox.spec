%define		plugin		lightbox
Summary:	DokuWiki Light Box v2 plugin
Summary(pl.UTF-8):	Wtyczka lightboxv2 dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20090312
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/downloads/glensc/dokuwiki-plugin-lightboxv2/lightboxv2-%{version}.tar.bz2
# Source0-md5:	52c942d8a13833e59141349fc15e124f
URL:		http://wiki.splitbrain.org/plugin:lightboxv2
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate LightBox v2 javascript animation in DokuWiki.

%prep
%setup -q -n %{plugin}v2
version=$(cat VERSION)
if [ $(echo "$version" | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(echo "$version" | tr -d -)
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{AUTHORS,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/images
