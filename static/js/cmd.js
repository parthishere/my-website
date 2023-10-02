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
    main: `Select a menu:<br><span onclick="handleMenuClick('1')">[1] Who is Parth?</span><br><span onclick="handleMenuClick('2')">[2] Contact me</span><br><span onclick="handleMenuClick('3')">[3] My works</span>`,
    1: `Who is Parth?<br><br>I have been learning embedded development for 4 years including developing drivers for I2C, Uart, USB and other sensors like gyro and accelerometer, Strong in problem solving, high level & low level system design. Software side have created projects that are solves some of the real world problems other than that, I have participated in hackathons and hardware-related ideathons and am excited about the opportunity to work with you.

    My goal is to continuously learn and apply new skills in the real world.<br><br><span onclick="handleMenuClick('B')">[B] Back</span>`,
    2: `Contact:<br>- Email: <a href="mailto:parthishere1234@gmail.com">parthishere1234@gmail.com</a><br>- Discord: <a href="https://discord.com/users/884890628511633459">@glizzykingdreko</a><br><br><span onclick="handleMenuClick('B')">[B] Back</span>`,
    3: `Some of my Projects:<br><br>
- <strong>DiscordWizard</strong>: A user-friendly Discord server mirrorer and cloner. <a href="https://github.com/glizzykingdreko/DiscordWizard" target="_blank">[GitHub]</a><br>
- <strong>CALINTRA</strong>: A Chrome extension designed for 42School students, enabling seamless synchronization of events with the page calendar. <a href="https://github.com/glizzykingdreko/CalIntra" target="_blank">[GitHub]</a><br>
- <strong>PerimeterX AST Deobfuscator</strong>: A tool to deobfuscate and understand PerimeterX's init script. <a href="https://github.com/glizzykingdreko/PerimeterX-Deobfuscator" target="_blank">[GitHub]</a><br>
- <strong>TMX AST Deobfuscator</strong>: A dedicated deobfuscator for TMX's dynamic scripts. <a href="https://github.com/glizzykingdreko/TMX-Deobfuscator" target="_blank">[GitHub]</a><br>
- <strong>Adyen 4.5.0 payment encryption in node</strong>: A node-based solution for secure payment encryption using Adyen 4.5.0. <a href="https://github.com/glizzykingdreko/adyen-4.5.0" target="_blank">[GitHub]</a> | <a href="https://github.com/glizzykingdreko/adyen-4.5.0" target="_blank">[v4.4.1]</a><br>
- <strong>TakionAPI</strong>: An industry-leading antibot bypass provider. <a href="https://takionapi.tech/github" target="_blank">[GitHub]</a> | <a href="https://Takionapi.tech/discord" target="_blank">[Discord]</a><br>
- <strong>This Landing Page</strong>: Check out the code and design of this landing page. <a href="https://codepen.io/glizzykingdreko" target="_blank">[CodePen]</a><br><br>
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

    if (currentMenu === "1" || currentMenu === "3") {
        speed = 1; // Makes the typing faster for "Who is glizzy".
        deleteSpeed = 1; // Makes the deletion faster for "Who is glizzy". Adjust as needed.
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
