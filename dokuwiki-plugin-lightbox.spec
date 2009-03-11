%define		plugin		lightbox
Summary:	DokuWiki Light Box v2 plugin
Summary(pl.UTF-8):	Wtyczka lightboxv2 dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20080808
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://laurent.beneytout.free.fr/lib/exe/fetch.php?media=projects:lightbox.zip
# Source0-md5:	1f28817f046b94c730f4a25a7c7b676e
URL:		http://wiki.splitbrain.org/plugin:lightboxv2
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate LightBox v2 javascript animation in DokuWiki.

%prep
%setup -q -n %{plugin}
rm -f images/Thumbs.db

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/images
