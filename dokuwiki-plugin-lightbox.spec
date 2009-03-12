%define		plugin		lightbox
Summary:	DokuWiki Light Box v2 plugin
Summary(pl.UTF-8):	Wtyczka lightboxv2 dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20080808
Release:	1.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.lokeshdhakar.com/projects/lightbox2/releases/lightbox2.04.zip
# Source0-md5:	c930f97a5791f202d7c48303de36f282
Patch0:		%{name}.patch
URL:		http://wiki.splitbrain.org/plugin:lightboxv2
BuildRequires:	sharutils
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate LightBox v2 javascript animation in DokuWiki.

%prep
%setup -qc -n %{plugin}
(
	cat js/prototype.js
	cat js/scriptaculous.js
	cat js/builder.js
	cat js/effects.js
	cat js/lightbox.js
) > script.js
%patch0 -p1
uudecode blank.gif.uue

rm -f images/bullet.gif
rm -f images/donate-button.gif
rm -f images/download-icon.gif
rm -f images/image-1.jpg
rm -f images/thumb-1.jpg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a images script.js $RPM_BUILD_ROOT%{plugindir}
cp -a css/lightbox.css $RPM_BUILD_ROOT%{plugindir}/screen.css

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
