(function () {
    "use strict";

    // Prevent the background from initializing more than once.
    if (window.__skillBridgeUniverseStarted) {
        return;
    }

    window.__skillBridgeUniverseStarted = true;

    // ============================================
    // CONFIGURATION
    // ============================================

    const REDUCED_MOTION = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    const PLANETS = [
        {
            name: "Mercury",
            orbit: 49,
            size: 3.5,
            speed: 0.34,
            phase: 0.4,
            light: "#e7e5e4",
            base: "#a8a29e",
            dark: "#44403c"
        },
        {
            name: "Venus",
            orbit: 78,
            size: 5,
            speed: 0.23,
            phase: 2.1,
            light: "#fef3c7",
            base: "#d6a65c",
            dark: "#854d0e"
        },
        {
            name: "Earth",
            orbit: 108,
            size: 6.2,
            speed: 0.17,
            phase: 4.2,
            light: "#93c5fd",
            base: "#2563eb",
            dark: "#172554",
            moon: true
        },
        {
            name: "Mars",
            orbit: 140,
            size: 4.7,
            speed: 0.125,
            phase: 1.7,
            light: "#fdba74",
            base: "#dc6546",
            dark: "#7f1d1d"
        },
        {
            name: "Jupiter",
            orbit: 182,
            size: 12,
            speed: 0.075,
            phase: 3.4,
            light: "#fde68a",
            base: "#d6a46d",
            dark: "#78350f",
            stripes: true
        },
        {
            name: "Saturn",
            orbit: 227,
            size: 10,
            speed: 0.055,
            phase: 5.1,
            light: "#fef3c7",
            base: "#d4b777",
            dark: "#78350f",
            rings: true
        },
        {
            name: "Uranus",
            orbit: 276,
            size: 7,
            speed: 0.039,
            phase: 0.8,
            light: "#cffafe",
            base: "#67cbd7",
            dark: "#164e63"
        },
        {
            name: "Neptune",
            orbit: 325,
            size: 7,
            speed: 0.029,
            phase: 2.8,
            light: "#c7d2fe",
            base: "#6366f1",
            dark: "#1e1b4b"
        }
    ];

    // ============================================
    // CREATE THE BACKGROUND CANVAS
    // ============================================

    let canvas = document.getElementById(
        "skillbridge-universe-canvas"
    );

    if (!canvas) {
        canvas = document.createElement("canvas");

        canvas.id = "skillbridge-universe-canvas";

        document.body.prepend(canvas);
    }

    canvas.setAttribute("aria-hidden", "true");

    Object.assign(canvas.style, {
        position: "fixed",
        inset: "0",
        width: "100%",
        height: "100%",
        zIndex: "0",
        pointerEvents: "none",
        userSelect: "none"
    });

    const ctx = canvas.getContext("2d", {
        alpha: false
    });

    if (!ctx) {
        console.error(
            "SkillBridge universe background could not initialize."
        );

        return;
    }

    // ============================================
    // STATE
    // ============================================

    let width = window.innerWidth;
    let height = window.innerHeight;
    let pixelRatio = 1;

    let stars = [];

    let elapsed = 0;
    let previousFrame = 0;

    let zoom = 1;
    let targetZoom = 1;

    let mouseX = 0;
    let mouseY = 0;

    let targetMouseX = 0;
    let targetMouseY = 0;

    const clamp = (value, min, max) => {
        return Math.min(max, Math.max(min, value));
    };

    // ============================================
    // STAR FIELD
    // ============================================

    function createStars() {
        const area = width * height;

        const starCount = Math.min(
            520,
            Math.max(140, Math.floor(area / 3000))
        );

        stars = [];

        for (let i = 0; i < starCount; i++) {
            const depth = Math.random();

            stars.push({
                x: Math.random() * width,
                y: Math.random() * height,

                depth: 0.15 + depth * 0.95,

                radius: 0.35 + depth * 1.1,

                twinkleSpeed: 0.5 + Math.random() * 2.0,

                phase: Math.random() * Math.PI * 2,

                drift: 2 + Math.random() * 9,

                color: Math.random() > 0.82
                    ? "#c4b5fd"
                    : Math.random() > 0.90
                        ? "#93c5fd"
                        : "#ffffff"
            });
        }
    }

    // ============================================
    // RESPONSIVE CANVAS
    // ============================================

    function resizeCanvas() {
        width = window.innerWidth;
        height = window.innerHeight;

        pixelRatio = Math.min(
            window.devicePixelRatio || 1,
            1.75
        );

        canvas.width = Math.floor(width * pixelRatio);
        canvas.height = Math.floor(height * pixelRatio);

        canvas.style.width = width + "px";
        canvas.style.height = height + "px";

        ctx.setTransform(
            pixelRatio,
            0,
            0,
            pixelRatio,
            0,
            0
        );

        createStars();

        updateScrollZoom();

        if (REDUCED_MOTION) {
            zoom = targetZoom;
            drawScene(0, 0);
        }
    }

    // ============================================
    // SCROLL ZOOM
    // ============================================

    function updateScrollZoom() {
        const documentHeight = Math.max(
            document.documentElement.scrollHeight,
            document.body.scrollHeight
        );

        const maxScroll = Math.max(
            0,
            documentHeight - window.innerHeight
        );

        const scrollProgress = maxScroll > 0
            ? clamp(window.scrollY / maxScroll, 0, 1)
            : 0;

        // Scrolling down zooms into space.
        // Scrolling back up zooms out.
        targetZoom = 1 + scrollProgress * 0.65;

        if (REDUCED_MOTION) {
            zoom = targetZoom;

            drawScene(0, 0);
        }
    }

    // ============================================
    // MOUSE MOVEMENT
    // ============================================

    function handlePointerMove(event) {
        targetMouseX = (
            event.clientX / Math.max(width, 1) - 0.5
        ) * 2;

        targetMouseY = (
            event.clientY / Math.max(height, 1) - 0.5
        ) * 2;

        if (REDUCED_MOTION) {
            mouseX = targetMouseX;
            mouseY = targetMouseY;

            drawScene(0, 0);
        }
    }

    function handlePointerLeave() {
        targetMouseX = 0;
        targetMouseY = 0;

        if (REDUCED_MOTION) {
            mouseX = 0;
            mouseY = 0;

            drawScene(0, 0);
        }
    }

    // ============================================
    // BACKGROUND GRADIENT
    // ============================================

    function drawSpaceBackground() {
        const gradient = ctx.createLinearGradient(
            0,
            0,
            width,
            height
        );

        gradient.addColorStop(0, "#020617");
        gradient.addColorStop(0.45, "#070b1e");
        gradient.addColorStop(1, "#030712");

        ctx.fillStyle = gradient;

        ctx.fillRect(0, 0, width, height);
    }

    // ============================================
    // NEBULA CLOUDS
    // ============================================

    function drawNebula(x, y, radius, colors) {
        const gradient = ctx.createRadialGradient(
            x,
            y,
            0,
            x,
            y,
            radius
        );

        gradient.addColorStop(0, colors[0]);
        gradient.addColorStop(0.35, colors[1]);
        gradient.addColorStop(0.72, colors[2]);
        gradient.addColorStop(1, "rgba(2, 6, 23, 0)");

        ctx.fillStyle = gradient;

        ctx.fillRect(
            x - radius,
            y - radius,
            radius * 2,
            radius * 2
        );
    }

    function drawNebulae(time, parallaxX, parallaxY) {
        const minDimension = Math.min(width, height);

        const driftX = Math.sin(time * 0.06) * 22;
        const driftY = Math.cos(time * 0.05) * 14;

        drawNebula(
            width * 0.22 + driftX + parallaxX * 0.5,
            height * 0.30 + driftY + parallaxY * 0.5,
            minDimension * 0.52,
            [
                "rgba(79, 70, 229, 0.19)",
                "rgba(79, 70, 229, 0.09)",
                "rgba(79, 70, 229, 0.025)"
            ]
        );

        drawNebula(
            width * 0.83 - driftY + parallaxX * 0.7,
            height * 0.67 + driftX + parallaxY * 0.5,
            minDimension * 0.48,
            [
                "rgba(124, 58, 237, 0.16)",
                "rgba(109, 40, 217, 0.07)",
                "rgba(109, 40, 217, 0.015)"
            ]
        );

        drawNebula(
            width * 0.52 + driftY,
            height * 0.06 + driftX,
            minDimension * 0.34,
            [
                "rgba(8, 145, 178, 0.09)",
                "rgba(14, 116, 144, 0.045)",
                "rgba(14, 116, 144, 0.01)"
            ]
        );
    }

    // ============================================
    // DISTANT STARS
    // ============================================

    function drawStars(time, parallaxX, parallaxY, currentZoom) {
        const centerX = width / 2;
        const centerY = height / 2;

        for (const star of stars) {
            const perspective = 0.35 + star.depth * 0.65;

            let x = centerX
                + (star.x - centerX) * perspective * currentZoom
                + parallaxX * star.depth * 0.85;

            let y = centerY
                + (star.y - centerY) * perspective * currentZoom
                + parallaxY * star.depth * 0.85;

            // Wrap stars around the viewport as the camera zooms.
            x = ((x % width) + width) % width;
            y = ((y % height) + height) % height;

            const twinkle = 0.45 + 0.55 * (
                (Math.sin(
                    time * star.twinkleSpeed + star.phase
                ) + 1) / 2
            );

            const radius = star.radius * (
                0.65 + star.depth * 0.55
            );

            ctx.globalAlpha = twinkle * (
                0.42 + star.depth * 0.5
            );

            ctx.fillStyle = star.color;

            ctx.beginPath();
            ctx.arc(x, y, radius, 0, Math.PI * 2);
            ctx.fill();

            // Add a subtle glow to the brighter stars.
            if (star.depth > 0.82 && radius > 1) {
                ctx.globalAlpha = twinkle * 0.18;

                ctx.beginPath();
                ctx.arc(x, y, radius * 3.2, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        ctx.globalAlpha = 1;
    }

    // ============================================
    // SHOOTING STARS
    // ============================================

    function drawShootingStars(time) {
        for (let i = 0; i < 2; i++) {
            const cycle = (
                time * 0.055 + i * 0.51
            ) % 1;

            // Each shooting star is visible briefly.
            if (cycle > 0.90) {
                const progress = (cycle - 0.90) / 0.10;

                const startX = width * (
                    0.12 + i * 0.53
                );

                const startY = height * (
                    0.10 + i * 0.17
                );

                const x = startX + progress * 180;
                const y = startY + progress * 110;

                const gradient = ctx.createLinearGradient(
                    x - 75,
                    y - 45,
                    x,
                    y
                );

                gradient.addColorStop(
                    0,
                    "rgba(165, 180, 252, 0)"
                );

                gradient.addColorStop(
                    1,
                    "rgba(224, 231, 255, 0.85)"
                );

                ctx.strokeStyle = gradient;
                ctx.lineWidth = 1.4;
                ctx.globalAlpha = Math.sin(progress * Math.PI);

                ctx.beginPath();
                ctx.moveTo(x - 75, y - 45);
                ctx.lineTo(x, y);
                ctx.stroke();

                ctx.globalAlpha = 1;
            }
        }
    }

    // ============================================
    // SOLAR SYSTEM CAMERA
    // ============================================

    function getSolarSystemCamera(parallaxX, parallaxY) {
        const smallScreen = width < 640;

        let unit = clamp(
            Math.min(width, height) / 900,
            0.4,
            1.05
        );

        if (smallScreen) {
            unit *= 0.76;
        }

        return {
            x: width * (smallScreen ? 0.62 : 0.69)
                + parallaxX * 23,

            y: height * 0.46
                + parallaxY * 17,

            unit: unit,
            scale: unit * zoom,
            tilt: -0.16
        };
    }

    // ============================================
    // ORBIT PATHS
    // ============================================

    function drawOrbits(camera) {
        ctx.save();

        ctx.translate(camera.x, camera.y);
        ctx.rotate(camera.tilt);

        for (let i = 0; i < PLANETS.length; i++) {
            const planet = PLANETS[i];

            const radius = planet.orbit * camera.scale;

            ctx.beginPath();

            ctx.ellipse(
                0,
                0,
                radius,
                radius * 0.39,
                0,
                0,
                Math.PI * 2
            );

            ctx.strokeStyle = i % 2 === 0
                ? "rgba(129, 140, 248, 0.14)"
                : "rgba(167, 139, 250, 0.10)";

            ctx.lineWidth = 1;

            ctx.stroke();
        }

        ctx.restore();
    }

    // ============================================
    // GLOWING SUN
    // ============================================

    function drawSun(x, y, radius, time) {
        const pulse = 1 + Math.sin(time * 1.2) * 0.035;

        // Outer glow.
        const outerGlow = ctx.createRadialGradient(
            x,
            y,
            radius * 0.25,
            x,
            y,
            radius * 6 * pulse
        );

        outerGlow.addColorStop(
            0,
            "rgba(251, 191, 36, 0.30)"
        );

        outerGlow.addColorStop(
            0.23,
            "rgba(249, 115, 22, 0.15)"
        );

        outerGlow.addColorStop(
            0.55,
            "rgba(234, 88, 12, 0.045)"
        );

        outerGlow.addColorStop(
            1,
            "rgba(234, 88, 12, 0)"
        );

        ctx.fillStyle = outerGlow;

        ctx.fillRect(
            x - radius * 6,
            y - radius * 6,
            radius * 12,
            radius * 12
        );

        // Inner corona.
        const corona = ctx.createRadialGradient(
            x - radius * 0.2,
            y - radius * 0.2,
            radius * 0.15,
            x,
            y,
            radius * 1.8
        );

        corona.addColorStop(
            0,
            "rgba(255, 250, 205, 0.95)"
        );

        corona.addColorStop(
            0.30,
            "rgba(251, 191, 36, 0.55)"
        );

        corona.addColorStop(
            1,
            "rgba(249, 115, 22, 0)"
        );

        ctx.fillStyle = corona;

        ctx.beginPath();
        ctx.arc(
            x,
            y,
            radius * 1.8 * pulse,
            0,
            Math.PI * 2
        );

        ctx.fill();

        // Solar disc.
        const sunGradient = ctx.createRadialGradient(
            x - radius * 0.35,
            y - radius * 0.38,
            radius * 0.05,
            x,
            y,
            radius
        );

        sunGradient.addColorStop(0, "#fff7cc");
        sunGradient.addColorStop(0.36, "#fde68a");
        sunGradient.addColorStop(0.72, "#f59e0b");
        sunGradient.addColorStop(1, "#c2410c");

        ctx.fillStyle = sunGradient;

        ctx.beginPath();
        ctx.arc(
            x,
            y,
            radius * pulse,
            0,
            Math.PI * 2
        );

        ctx.fill();

        // Bright highlight.
        ctx.fillStyle = "rgba(255, 255, 255, 0.45)";

        ctx.beginPath();
        ctx.ellipse(
            x - radius * 0.25,
            y - radius * 0.34,
            radius * 0.20,
            radius * 0.12,
            -0.5,
            0,
            Math.PI * 2
        );

        ctx.fill();
    }

    // ============================================
    // PLANET RINGS
    // ============================================

    function drawPlanetRings(x, y, radius) {
        ctx.save();

        ctx.translate(x, y);
        ctx.rotate(-0.33);

        // Back ring.
        ctx.beginPath();

        ctx.ellipse(
            0,
            0,
            radius * 1.95,
            radius * 0.61,
            0,
            0,
            Math.PI * 2
        );

        ctx.strokeStyle = "rgba(253, 230, 138, 0.55)";
        ctx.lineWidth = Math.max(1, radius * 0.17);

        ctx.stroke();

        ctx.beginPath();

        ctx.ellipse(
            0,
            0,
            radius * 1.70,
            radius * 0.51,
            0,
            0,
            Math.PI * 2
        );

        ctx.strokeStyle = "rgba(217, 180, 112, 0.42)";
        ctx.lineWidth = Math.max(0.6, radius * 0.09);

        ctx.stroke();

        ctx.restore();
    }

    // ============================================
    // PLANET SPHERES
    // ============================================

    function drawPlanetSphere(x, y, radius, planet) {
        const gradient = ctx.createRadialGradient(
            x - radius * 0.36,
            y - radius * 0.40,
            radius * 0.08,
            x + radius * 0.12,
            y + radius * 0.12,
            radius * 1.35
        );

        gradient.addColorStop(0, planet.light);
        gradient.addColorStop(0.38, planet.base);
        gradient.addColorStop(0.78, planet.dark);
        gradient.addColorStop(1, "#020617");

        // Subtle atmospheric glow.
        ctx.globalAlpha = 0.22;

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            radius * 1.35,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = planet.light;
        ctx.fill();

        ctx.globalAlpha = 1;

        // Planet body.
        ctx.beginPath();

        ctx.arc(
            x,
            y,
            radius,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = gradient;
        ctx.fill();

        ctx.strokeStyle = "rgba(255, 255, 255, 0.20)";
        ctx.lineWidth = Math.max(0.5, radius * 0.06);

        ctx.stroke();

        // Jupiter's subtle cloud bands.
        if (planet.stripes && radius > 3) {
            ctx.save();

            ctx.beginPath();

            ctx.arc(
                x,
                y,
                radius * 0.98,
                0,
                Math.PI * 2
            );

            ctx.clip();

            ctx.strokeStyle = "rgba(120, 53, 15, 0.30)";
            ctx.lineWidth = Math.max(1, radius * 0.16);

            for (let i = -1; i <= 1; i++) {
                ctx.beginPath();

                ctx.ellipse(
                    x,
                    y + i * radius * 0.38,
                    radius * 0.96,
                    radius * 0.17,
                    0,
                    0,
                    Math.PI * 2
                );

                ctx.stroke();
            }

            ctx.restore();
        }

        // Highlight.
        ctx.fillStyle = "rgba(255, 255, 255, 0.15)";

        ctx.beginPath();

        ctx.ellipse(
            x - radius * 0.25,
            y - radius * 0.33,
            radius * 0.24,
            Math.max(0.5, radius * 0.12),
            -0.5,
            0,
            Math.PI * 2
        );

        ctx.fill();
    }

    // ============================================
    // EARTH'S MOON
    // ============================================

    function drawMoon(x, y, radius, time) {
        const moonAngle = time * 0.7;

        const moonX = x + Math.cos(moonAngle) * radius * 1.8;
        const moonY = y + Math.sin(moonAngle) * radius * 1.3;

        ctx.beginPath();

        ctx.arc(
            moonX,
            moonY,
            Math.max(1, radius * 0.24),
            0,
            Math.PI * 2
        );

        ctx.fillStyle = "#e2e8f0";
        ctx.fill();

        ctx.strokeStyle = "rgba(255, 255, 255, 0.28)";
        ctx.lineWidth = 0.5;

        ctx.stroke();
    }

    // ============================================
    // PLANET POSITIONING
    // ============================================

    function getPlanetPositions(camera, time) {
        const positions = [];

        for (const planet of PLANETS) {
            const angle = time * planet.speed + planet.phase;

            const horizontal = (
                Math.cos(angle) *
                planet.orbit *
                camera.scale
            );

            const vertical = (
                Math.sin(angle) *
                planet.orbit *
                camera.scale *
                0.39
            );

            // Tilt the orbital plane to add perspective.
            const rotatedX = (
                horizontal * Math.cos(camera.tilt) -
                vertical * Math.sin(camera.tilt)
            );

            const rotatedY = (
                horizontal * Math.sin(camera.tilt) +
                vertical * Math.cos(camera.tilt)
            );

            const depth = Math.sin(angle);

            const perspectiveScale = 0.88 + depth * 0.12;

            positions.push({
                planet: planet,

                x: camera.x + rotatedX,

                y: camera.y + rotatedY,

                radius: Math.max(
                    1.5,
                    planet.size *
                    camera.unit *
                    zoom *
                    perspectiveScale
                ),

                depth: depth
            });
        }

        // Planets nearer the bottom are drawn later,
        // giving the impression of depth in the orbital plane.
        positions.sort(function (a, b) {
            return a.y - b.y;
        });

        return positions;
    }

    // ============================================
    // DRAW COMPLETE SOLAR SYSTEM
    // ============================================

    function drawSolarSystem(time, parallaxX, parallaxY) {
        const camera = getSolarSystemCamera(
            parallaxX,
            parallaxY
        );

        const sunRadius = Math.max(
            7,
            16 * camera.scale
        );

        // Draw the orbital paths first.
        drawOrbits(camera);

        // Draw the Sun in the center.
        drawSun(
            camera.x,
            camera.y,
            sunRadius,
            time
        );

        // Draw planets in depth order.
        const planetPositions = getPlanetPositions(
            camera,
            time
        );

        for (const position of planetPositions) {
            const planet = position.planet;

            // Saturn's rings sit behind its sphere.
            if (planet.rings) {
                drawPlanetRings(
                    position.x,
                    position.y,
                    position.radius
                );
            }

            drawPlanetSphere(
                position.x,
                position.y,
                position.radius,
                planet
            );

            // Add a small moon to Earth.
            if (planet.moon) {
                drawMoon(
                    position.x,
                    position.y,
                    position.radius,
                    time
                );
            }
        }

        // Soft system-wide glow.
        const ambientGlow = ctx.createRadialGradient(
            camera.x,
            camera.y,
            sunRadius,
            camera.x,
            camera.y,
            350 * camera.scale
        );

        ambientGlow.addColorStop(
            0,
            "rgba(99, 102, 241, 0.035)"
        );

        ambientGlow.addColorStop(
            1,
            "rgba(99, 102, 241, 0)"
        );

        ctx.fillStyle = ambientGlow;

        ctx.fillRect(
            camera.x - 350 * camera.scale,
            camera.y - 350 * camera.scale,
            700 * camera.scale,
            700 * camera.scale
        );
    }

    // ============================================
    // COMPLETE BACKGROUND RENDER
    // ============================================

    function drawScene(time, deltaTime) {
        ctx.clearRect(0, 0, width, height);

        drawSpaceBackground();

        // Move distant stars slightly for parallax depth.
        drawNebulae(
            time,
            mouseX * 20,
            mouseY * 16
        );

        drawStars(
            time,
            mouseX * 28,
            mouseY * 20,
            zoom
        );

        drawShootingStars(time);

        drawSolarSystem(
            time,
            mouseX,
            mouseY
        );

        // Reset drawing state to avoid leaking styles.
        ctx.globalAlpha = 1;
        ctx.globalCompositeOperation = "source-over";
    }

    // ============================================
    // ANIMATION LOOP
    // ============================================

    function animate(timestamp) {
        if (!previousFrame) {
            previousFrame = timestamp;
        }

        const deltaTime = Math.min(
            (timestamp - previousFrame) / 1000,
            0.05
        );

        previousFrame = timestamp;

        elapsed += deltaTime;

        // Smooth camera zoom.
        zoom += (targetZoom - zoom) * 0.035;

        // Smooth mouse-controlled movement.
        mouseX += (targetMouseX - mouseX) * 0.045;
        mouseY += (targetMouseY - mouseY) * 0.045;

        drawScene(elapsed, deltaTime);

        if (!REDUCED_MOTION) {
            requestAnimationFrame(animate);
        }
    }

    // ============================================
    // EVENT LISTENERS
    // ============================================

    window.addEventListener(
        "resize",
        resizeCanvas,
        { passive: true }
    );

    window.addEventListener(
        "scroll",
        updateScrollZoom,
        { passive: true }
    );

    window.addEventListener(
        "pointermove",
        handlePointerMove,
        { passive: true }
    );

    document.addEventListener(
        "pointerleave",
        handlePointerLeave
    );

    // ============================================
    // START
    // ============================================

    resizeCanvas();

    if (REDUCED_MOTION) {
        drawScene(0, 0);
    } else {
        requestAnimationFrame(animate);
    }

})();