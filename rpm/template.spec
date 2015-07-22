Name:           ros-indigo-ecl-core
Version:        0.61.1
Release:        0%{?dist}
Summary:        ROS ecl_core package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ecl_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-ecl-command-line
Requires:       ros-indigo-ecl-concepts
Requires:       ros-indigo-ecl-containers
Requires:       ros-indigo-ecl-converters
Requires:       ros-indigo-ecl-core-apps
Requires:       ros-indigo-ecl-devices
Requires:       ros-indigo-ecl-eigen
Requires:       ros-indigo-ecl-exceptions
Requires:       ros-indigo-ecl-formatters
Requires:       ros-indigo-ecl-geometry
Requires:       ros-indigo-ecl-ipc
Requires:       ros-indigo-ecl-linear-algebra
Requires:       ros-indigo-ecl-math
Requires:       ros-indigo-ecl-mpl
Requires:       ros-indigo-ecl-sigslots
Requires:       ros-indigo-ecl-statistics
Requires:       ros-indigo-ecl-streams
Requires:       ros-indigo-ecl-threads
Requires:       ros-indigo-ecl-time
Requires:       ros-indigo-ecl-type-traits
Requires:       ros-indigo-ecl-utilities
BuildRequires:  ros-indigo-catkin

%description
A set of tools and interfaces extending the capabilities of c++ to provide a
lightweight, consistent interface with a focus for control programming.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

