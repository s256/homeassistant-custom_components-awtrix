# homeassistant-custom_components-awtrix
Homeassistant [awtrix](https://blueforcer.github.io/awtrix3/#/) Integration - Forked from [https://github.com/10der/homeassistant-custom_components-awtrix/tree/main](https://github.com/10der/homeassistant-custom_components-awtrix/tree/main)
I forked it because [041aa27](https://github.com/10der/homeassistant-custom_components-awtrix/commit/041aa2751fb37f5ea4f9b1debe10839fd70841ff) broke the weather integration.

## Setup 
Add `https://github.com/s256/homeassistant-custom_components-awtrix` to [HACS](https://hacs.xyz/) via Custom Repository as Integration.

After installing the custom compontent, add the integration either:


add 

```
awtrix:
```
to the `configuraiton.yaml` file

or add the integration via `Settings` -> `Devices & Services` -> `+Add Integration` and select `Awtrix tools and notifications`.


## Examples

```
service: notify.awtrix_bedroom
data:
  message: The garage door has been open for 10 minutes.
```


```
service: awtrix.awtrix_bedroom_push_app_data
data: 
  name: test
  data:
    text : "Hello, AWTRIX Light!"
    rainbow: true
    icon: "87"
    duration: 5
    pushIcon: 2
    lifetime: 900
    repeat: 1
```


```
service: notify.awtrix_bedroom
data:
  message: The garage door has been open for 10 minutes.
  data:
    icon: "33655"
    sound: beep
```


```
service: awtrix.awtrix_bedroom_weather_app
data:
 weather: weather.forecast_home
 outside_temperature: sensor.easyweatherv1_6_4_outdoor_temperature
 home_temperature: sensor.home_temperature
 moon: sensor.moon_phase
 sun: sun.sun
```

- no need to upload icons
- able to customize icons

```
service: awtrix.awtrix_bedroom_weather_app
data:
  weather: weather.forecast_home
  outside_temperature: sensor.easyweatherv1_6_4_outdoor_temperature
  home_temperature: sensor.home_temperature
  sun: sun.sun
  moon: sensor.moon_phase
  icons:
      clear-night: "a12181" 
      cloudy: "a2283"
      exceptional: "a2364"
      fog: "17056"
      hail: "a2441" 
      lightning: "a630" 
      lightning-rainy: "a49299" 
      partlycloudy: "a2286" 
      pouring: "a49300" 
      rainy: "a2284" 
      snowy: "a2289" 
      snowy-rainy: "a49301" 
      sunny: "a2282" 
      windy: "a15618" 
      windy-variant: "a15618" 
      full_moon: "2314" 
      waning_gibbous: "2315" 
      last_quarter: "2316" 
      waning_crescent: "2317" 
      new_moon: "2318"
      waxing_crescent: "2320" 
      first_quarter: "2320" 
      waxing_gibbous: "36234" 
      home:  "96"
      sunrise: "485" 
      sunset: "486" 
      unavailable:  "52176"
```