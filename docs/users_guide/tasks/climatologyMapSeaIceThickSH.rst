.. _task_climatologyMapSeaIceThickSH:

climatologyMapSeaIceThickSH
===========================

An analysis task for plotting maps of Antarctic sea ice thickness against
observations.  Cell-averaged thickness is plotted (rather than thickness
averaged over the sea ice-covered area).

Component and Tags::

  component: seaIce
  tags: climatology, horizontalMap, seaIceThick, publicObs

Configuration Options
---------------------

The following configuration options are available for this task::

  [climatologyMapSeaIceThickSH]
  ## options related to plotting horizontally remapped climatologies of
  ## sea ice thickness against reference model results and observations
  ## in the southern hemisphere (SH)

  # colormap for model/observations
  colormapNameResult = ice
  # color indices into colormapName for filled contours
  colormapIndicesResult = [20, 80, 110, 140, 170, 200, 230, 255]
  # colormap levels/values for contour boundaries
  colorbarLevelsResult = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2, 2.5]

  # colormap for differences
  colormapNameDifference = balance
  # color indices into colormapName for filled contours
  colormapIndicesDifference = [0, 32, 64, 96, 128, 128, 160, 192, 224, 255]
  # colormap levels/values for contour boundaries
  colorbarLevelsDifference = [-3., -2.5, -2, -0.5, -0.1, 0, 0.1, 0.5, 2, 2.5, 3.]

  # Months or seasons to plot (These should be left unchanged, since
  # observations are only available for these seasons)
  seasons =  ['FM', 'ON']

  # comparison grid(s) ('latlon', 'antarctic') on which to plot analysis
  comparisonGrids = ['latlon']

  # reference lat/lon for sea ice plots in the northern hemisphere
  minimumLatitude = -50
  referenceLongitude = 180

  # a list of prefixes describing the sources of the observations to be used
  observationPrefixes = ['']

  # arrange subplots vertically?
  vertical = False

  # observations files
  thicknessSH_ON = ICESat/ICESat_gridded_mean_thickness_SH_on.interp0.5x0.5_20180710.nc
  thicknessSH_FM = ICESat/ICESat_gridded_mean_thickness_SH_fm.interp0.5x0.5_20180710.nc

The option ``minimumLatitude`` determines what the northernmost latitude (in
degrees) included in the plot will be.  The option ``referenceLongitude``
defines which longitude will be at the bottom of the plot.

The option ``observationPrefixes`` should be left as a list of the empty
string and is included for allowing easy code reuse with the
``climatologyMapSeaIceConc*`` tasks.

The option ``vertical = True`` can be used to plot 3 panels one above another
(resulting in a tall, thin image) rather than next to each other, the default
(resulting in a short, wide image).

The ability to modify observations files pointed to by ``thicknessSH_ON`` and
``thicknessSH_FM`` is provided for debugging purposes and these options
should typically remain unchanged.

For details on the remaining configration options, see:
 * :ref:`config_colormaps`
 * :ref:`config_seasons`
 * :ref:`config_comparison_grids`

Observations
------------

:ref:`icesat_thickness`

Example Result
--------------

.. image:: examples/ice_thick_sh.png
   :width: 720 px
   :align: center
