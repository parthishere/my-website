const currentDate = new Date();
const formattedDate =
    currentDate.toDateString().split(" ").slice(0, 3).join(" ") +
    " " +
    currentDate.toTimeString().split(" ")[0].split(":").slice(0, 3).join(":");
document.getElementById("dateTime").innerHTML = formattedDate;
const typingElement = document.querySelector(".typing");
let index = 0;
let currentText = "";
let isDeleting = false;
let currentMenu = "main";

const menus = {
    main: `Select a menu:<br><span onclick="handleMenuClick('1')">[1] Who is Parth?</span><br><span onclick="handleMenuClick('2')">[2] Contact me</span><br><span onclick="handleMenuClick('3')">[3] Hardware Projects</span><br><span onclick="handleMenuClick('4')">[4] Software Projects</span><br><span onclick="handleMenuClick('5')">[5] Work Experience</span><br><span onclick="handleMenuClick('6')">[6] Skills & Technologies</span>`,
    
    1: `Who is Parth?<br><br>I have been learning embedded development for 4+ years including developing drivers for I2C, UART, USB and sensors like gyro and accelerometer. Strong in problem solving, high level & low level system design. I have created projects that solve real world problems and participated in hackathons and hardware-related ideathons.<br><br>Currently pursuing M.S in Electrical and Computer Engineering (Specialization: Embedded Systems) at University of Colorado Boulder. Previously worked as BIOS Firmware Engineer Intern at AMD and Embedded Developer at various companies.<br><br>My goal is to continuously learn and apply new skills in the real world.<br><br><span onclick="handleMenuClick('B')">[B] Back</span>`,
    
    2: `Contact:<br>- Email: <a href="mailto:parthishere1234@gmail.com">parthishere1234@gmail.com</a><br>- LinkedIn: <a href="https://linkedin.com/in/parth-thakkar-819616197">LinkedIn Profile</a><br>- Phone: <a href="tel:+13035489344">+1 303-548-9344</a><br>- Location: Boulder, Colorado, US<br><br><span onclick="handleMenuClick('B')">[B] Back</span>`,
    
    3: `Hardware Projects:<br><br>
<strong>• 8-bit CPU from Logic Gates</strong>: TTL-based CPU with Program Counter, ALU, Control Unit, 16-byte RAM. Runs Fibonacci, addition, subtraction at 300Hz.<br>
<strong>• Pong Game with 8051</strong>: 16x32 pixel display, PS2 controller interface, real-time collision detection.<br>
<strong>• 6052 Computer Simulator</strong>: C++ simulator with virtual memory, complete instruction set. <a href="https://github.com/parthishere/6052-emulator" target="_blank">[GitHub]</a><br>
<strong>• 16-bit CPU in HDL</strong>: NAND2Tetris CPU running Pong & Space Invaders. <a href="https://github.com/parthishere/16Bit-HDL-CPU_Simulation" target="_blank">[GitHub]</a><br>
<strong>• IoT Ecosystem</strong>: Django+ESP32+PostgreSQL, GPS tracking, HTTPS/WebSocket. <a href="https://fleetkaptan.up.railway.app" target="_blank">[Demo]</a><br>
<strong>• Baremetal RTOS</strong>: Custom RTOS for STM32F070, Round Robin/Cooperative scheduling. <a href="https://github.com/parthishere/RTOS-from-scratch" target="_blank">[GitHub]</a><br>
<strong>• KL25Z Drivers</strong>: ARM Cortex M0+ drivers (UART, PWM, DMA, DAC), 400ms→82ms optimization.<br>
<strong>• Autonomous Car</strong>: Lane detection, object avoidance (TensorFlow, OpenCV, RPi).<br>
<strong>• PCB Design Labs</strong>: Astable multivibrator, Golden Arduino (10-20% noise reduction). <a href="https://github.com/parthishere/PCB-design" target="_blank">[GitHub]</a><br><br>
<span onclick="handleMenuClick('B')">[B] Back</span>`,
    
    4: `Software Projects:<br><br>
<strong>• LogUp - Face Recognition Attendance</strong>: Django+TensorFlow, AWS deployment, real-time tracking. <a href="https://facelogup.herokuapp.com" target="_blank">[Demo]</a><br>
<strong>• Web-meetup Video Chat</strong>: WebRTC+Django+Redis, screen sharing, file transfer. <a href="https://github.com/parthishere/videochat" target="_blank">[GitHub]</a><br>
<strong>• DevMedia Social Platform</strong>: Developer-focused social media, GraphQL+Celery. <a href="https://devmediaonapi.herokuapp.com" target="_blank">[Demo]</a><br>
<strong>• KeeponNote</strong>: React+Django notes app with Google/GitHub auth. <a href="https://notesonhand.netlify.app" target="_blank">[Demo]</a><br>
<strong>• Event QR Generator</strong>: Mass QR code generation, email distribution, pass scanning. <a href="https://github.com/parthishere/qrcode" target="_blank">[GitHub]</a><br>
<strong>• ML Models from Scratch</strong>: Neural Networks, Decision Tree, RCNN, LENET-5. <a href="https://github.com/parthishere/RCNN-and-LENET-5" target="_blank">[GitHub]</a><br>
<strong>• IoT Home Automation</strong>: Telegram bot + ESP8266 integration. <a href="https://github.com/parthishere/ESP8266" target="_blank">[GitHub]</a><br><br>
<span onclick="handleMenuClick('B')">[B] Back</span>`,
    
    5: `Work Experience:<br><br>
<strong>• BIOS Firmware Engineer Intern - AMD</strong> (May 2024 - Aug 2024)<br>
  - IoT charger design, PCB manufacturing, AWS server management<br>
  - OCPP/MQTT protocols, custom LCD/GPS drivers<br><br>
<strong>• Embedded Developer Intern - Griden Power</strong> (Sep 2022 - May 2023)<br>
  - EV charger IoT components, wireless communication systems<br>
  - Airport hygiene monitoring with ESP cloud integration<br><br>
<strong>• Firmware Developer Intern - Scan Point Geomatics</strong> (Oct 2022 - Aug 2023)<br>
  - UHF-RFID driver development, algorithm optimization<br>
  - Full product design: PCB + 3D printing + ESP32 integration<br><br>
<strong>• Python Developer - Citrus Tech</strong> (2021)<br>
  - Cryptocurrency market making bot for CITRUS coin<br><br>
<strong>• Hardware Team - Club Robocon</strong> (Mar 2019 - Sep 2019)<br>
  - DD Robocon India robot baremetal drivers<br>
  - ATmega328p: I2C, UART, SPI, PID controllers, MATLAB simulation<br><br>
<span onclick="handleMenuClick('B')">[B] Back</span>`,
    
    6: `Skills & Technologies:<br><br>
<strong>Programming Languages (Expert 96%):</strong><br>
• Embedded C, C++, Assembly (ARM/AVR/8051/6502)<br>
• Python & Django<br>
• JavaScript & jQuery<br><br>
<strong>Programming Languages (Pro 86%):</strong><br>
• MicroPython, HDL/VHDL, MATLAB<br>
• Linux Administration, Shell scripting<br><br>
<strong>Frameworks & Libraries:</strong><br>
• Django REST, GraphQL, Celery, WebRTC<br>
• TensorFlow, OpenCV, Keras, React<br><br>
<strong>Hardware & Protocols:</strong><br>
• PCB Design, ARM/AVR/ESP32, FPGA programming<br>
• UART, SPI, I2C, USB, MQTT, OCPP, BLE, RFID<br><br>
<strong>Tools & Platforms:</strong><br>
• AWS, Docker, Git, MCUXpresso, STM32CubeIDE<br>
• KiCad, Eagle, Proteus, Oscilloscopes<br><br>
<span onclick="handleMenuClick('B')">[B] Back</span>`
};

function handleMenuClick(menuKey) {
    if (menuKey in menus && currentMenu !== menuKey) {
        isDeleting = true;
        typeDeleteAnimation(() => {
            currentMenu = menuKey;
            currentText = menus[menuKey];
            index = 0;
            typeDeleteAnimation();
        });
    } else if ((menuKey === "B" || menuKey === "b") && currentMenu !== "main") {
        isDeleting = true;
        typeDeleteAnimation(() => {
            currentMenu = "main";
            currentText = menus.main;
            index = 0;
            typeDeleteAnimation();
        });
    }
}
function typeDeleteAnimation(callback) {
    let speed = 7; // default typing speed
    let deleteSpeed = 3; // default deletion speed

    if (currentMenu === "1" || currentMenu === "3" || currentMenu === "4" || currentMenu === "5" || currentMenu === "6") {
        speed = 1; // Makes the typing faster for longer content
        deleteSpeed = 1; // Makes the deletion faster for longer content
    }

    if (isDeleting && typingElement.innerHTML !== "") {
        if (currentText.charAt(index - 1) === ">") {
            const openTagIndex = currentText.lastIndexOf("<", index);
            const tagName = currentText.substring(
                openTagIndex + 1,
                currentText.indexOf(" ", openTagIndex)
            );
            const startTagIndex = currentText.lastIndexOf(
                `</${tagName}>`,
                index
            );
            index = startTagIndex;
        } else {
            index--;
        }
        currentText = currentText.slice(0, index);
        typingElement.innerHTML = currentText;

        setTimeout(() => typeDeleteAnimation(callback), deleteSpeed);
    } else if (isDeleting) {
        isDeleting = false;
        if (callback) callback();
    } else if (!isDeleting && index < currentText.length) {
        if (currentText.charAt(index) === "<") {
            if (currentText.substr(index, 4) === "<br>") {
                const br = document.createElement("br");
                typingElement.appendChild(br);
                index += 4;
            } else {
                const closingTagIndex = currentText.indexOf(">", index);
                const tagName = currentText
                    .substring(index + 1, closingTagIndex)
                    .split(" ")[0];
                const endTagIndex =
                    currentText.indexOf(`</${tagName}>`, index) +
                    `</${tagName}>`.length;
                const outerHTML = currentText.substring(index, endTagIndex);
                const tempDiv = document.createElement("div");
                tempDiv.innerHTML = outerHTML;
                const childElement = tempDiv.firstChild;

                if (tagName === "a") {
                    childElement.target = "_blank";
                    speed = 1; // Faster typing for <a> tag
                } else if (tagName === "span") {
                    childElement.onclick = function () {
                        const menuKey = childElement
                            .getAttribute("onclick")
                            .replace("handleMenuClick('", "")
                            .replace("')", "");
                        handleMenuClick(menuKey);
                    };
                    speed = 1; // Faster typing for <span> tag
                }

                typingElement.appendChild(childElement);
                index = endTagIndex;
            }
        } else {
            typingElement.innerHTML += currentText.charAt(index);
            index++;
        }

        setTimeout(typeDeleteAnimation, speed);
    }
}

function handleUserInput(event) {
    const key = event.key;
    if (key in menus && currentMenu !== key) {
        isDeleting = true;
        typeDeleteAnimation(() => {
            currentMenu = key;
            currentText = menus[key];
            index = 0;
            typeDeleteAnimation();
        });
    } else if ((key === "B" || key === "b") && currentMenu !== "main") {
        isDeleting = true;
        typeDeleteAnimation(() => {
            currentMenu = "main";
            currentText = menus.main;
            index = 0;
            typeDeleteAnimation();
        });
    }
}

document.addEventListener("keydown", handleUserInput);

// Initialize the typing animation with the main menu on page load
currentText = menus.main;
typeDeleteAnimation();
