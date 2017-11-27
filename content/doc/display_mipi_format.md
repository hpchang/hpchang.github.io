Title: Display Serial Interface (DSI) by MIPI
Date: 2017-10-12 00:00
Modified: 2017-11-27 00:00
Category: display
Tags: display, display interface, mipi
Slug: display-mipi-format
lang: en
Authors: HP Chang
Summary: Introduction to Display Serial Interface MIPI




One of the biggest change in mobile technology is higher display resolustion with faster interface. I would like to describe how image content transfer from digital binary to pixel’s crystal. This article is motivated by many discussions with Chun-Hsi, Bowen and Scott.

<img src="{filename}/res/tablet-313002_1280.jpg" alt="Figure tablet display" title="Tablet display by Mocho on pixabay" style="width: 640px;" />

_Image source via Mocho by [pixabay](https://pixabay.com/en/tablet-screen-monitor-phone-pc-313002/)_

## Overview of Display System

Let's look inside of a thin-film transistor(TFT) LCD [^LCD] panel:

* TFTs are subjected to varying voltages to change orientation of molecules in the liquid crystal suspension. This adjust the amount of light allowed to pass through, thereby changing the colour picture.
* Each unit pixel has a TFT, a pixel electrode (IT0), and a storage capacitor (Cs). 
* Each is individually addressable from the pads at the ends of the rows and columns connecting through the matrix.

[^LCD]: "liquid crystal display: active-matrix TFT liquid crystal display". Illustration. [Encyclopædia Britannica Online. Web. 27 Nov. 2017](https://www.britannica.com/technology/liquid-crystal-display?oasmId=60170)

The job of display driving IC is to receive digital data from host and control associated timing and voltage of each pixel on matrix TFT panel. Above is all about physical control. Let's look at how we achieve so fast digital transmission from frame data. 

![enter image description here](https://lh3.googleusercontent.com/a6LGieR1SQvd279gX7koknqjzUKxsDzpnYJJ7Ss1wJGxuJjVenXLqI2Ul03U75EwiEMFc1DkxsJDeg=s600)

_Image source via MIPI introduction by Ryan_

[The mobile market, specifically smartphones, has been growing immensely in the past 10 years while MIPI CSI-2 and DSI have been the interfaces of choice to enable multiple cameras and some displays in mobile devices...Both interfaces utilize the same physical layer – MIPI D-PHY – to transmit data to the application processor or SoC.](https://www.synopsys.com/designware-ip/technical-bulletin/implementing-mipi-camera.html)

Taking the Qualcomm S805(image[^S805_syna_image], table#1[^S805_table_1]) as example. Due to 1440x2560x32bppx60fps picture bandwidth, it uses two **DSI** ports(D-PHY 1.01, 1.0Gbps/lane) with 4 lanes each to drive the display in halves of 720×2560 pixels as below figure.

[^S805_syna_image]: [R63319 display driver support 1440x2560](http://www.turnhardware.net/?p=10088)

[^S805_table_1]: Table 1: Typical display resolutions supported in mobile devices using MIPI DSI and D-PHY from ["Choose the Right Storage, Display Interfaces for Low-Power Mobile SoCs" by Hezi Saar](https://lh3.googleusercontent.com/oQUU9Bm65VA53Q9O5WEmFQtS4kbLlEptwRAoU9r9ex_iGoMY_PaHHA8SL9cIo4ZU9RfEQnj7L0ePxQ=s1000)

## DSI Video mode

Video mode refers to transactions taking the form of a real-time pixel stream. The host provides video data, that is, pixel values, and synchronization information, that is, Vsync, Hsync, data enable, and the pixel clock.

![enter image description here](https://lh3.googleusercontent.com/LoBKDYQEDrzuT67NSFFhF5Q27XzYol7pbmovHW6RCNCeRTtfn9KTLYuQ9bu9LWx2_cRsgVVFQcHIFw)

_Image source via Qualcomm DSI Programming Guide LM80-P0598-2_ 

Let’s see the timing details associated in transmitting the video frame by RGB888 video format in 640×480 display[^RGB888]

[^RGB888]: [In RGB888 data format, each pixel has 3 bytes (24bits) of information, 1byte (8bits) for each component (R and G and B).  In 640×480 resolution frame, each line has 640 pixels and frame has 480 lines. Let’s see the timing information which needs to be sent along with this RGB data. Every video frame should have below information (in the order of sequence)](https://blogs.synopsys.com/vip-central/2015/02/10/video-frame-transmission-in-mipi-dsi/) i.e. VSYNC (Sync information), VBP (Vertical back porch timing information), VACT (Active video data along with horizontal back porch and front porch timing), VFP (Vertical front porch timing information)

Then, we transfer above 2D timing info to serial DSI packet(VSS,HSS,RGB) on one video frame. As packet pixel stream(0x3E) inside a frame, packet is described with "data type", "word count", "24bpp" and "CRC. Those bytes of packet data are alignment with 4 DSI Data lines configuration(MIPI D-PHY).  

![enter image description here](https://lh3.googleusercontent.com/AaNkGJmC2wDEoqNQD0P70EJNDwTyzee9b0FHtGjpAf7rUOubLSz_q_VbyZWmyEJSqQylXHpTIK-jvQ=s1280)

_Image source via datasheet of TI SN65DSI84 and STM AN4860_

## DSI Command mode
Besides video mode of DSI, **command mode** of DSI is used to send DCS command(0x5) to control display behavior i.e. sleep in/out. There are short and long packet to support command mode and the format is described as follows.

- Short packet issues DCS sleep in command i.e. 0x05 0x10
- Long packet issues DCS long write(0x39) 
![enter image description here](https://lh3.googleusercontent.com/a46M1QLJ6HaE3gNjXH_whL_JcrzRnIMunGmrC0me5eXlwoTcbrw4Y6eQE04qXcYHlXVdfiCZnPmamQ=s1200)

_Image source via datasheet of ILITEK ILI9806E_

## Touch Disaply Driver Integration(TDDI)

We recognize the format from host to device. Now let's look it further to TDDI case.
Switching of the crystals in the LCD for display update functions lead to noises on the touch sensing. 
Synaptics' TDsync [^TDsync] technology synchronizes their active period, thus avoiding display noise. 

[^TDsync]: [The superior touch performance enabled by TDsync technology is available with Synaptics In-Cell
touchscreen controller implementations. Focused engineering investments and strategic acquisitions have
made Synaptics the industry leader in display integration.](http://www.synaptics.com/sites/default/files/tdsync-eliminates-smartphone-tablet-display-noise.pdf) 

