document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.getElementById("mobile-menu-button");
    const mobileMenu = document.getElementById("mobile-menu");

    const openIcon = document.getElementById("menu-open-icon");
    const closeIcon = document.getElementById("menu-close-icon");

    const header = document.getElementById("site-header");


    /*
    |--------------------------------------------------------------------------
    | MOBILE MENU
    |--------------------------------------------------------------------------
    */

    if (menuButton && mobileMenu) {
        menuButton.addEventListener("click", () => {

            const isCurrentlyOpen =
                !mobileMenu.classList.contains("hidden");

            mobileMenu.classList.toggle("hidden");

            openIcon?.classList.toggle(
                "hidden",
                !isCurrentlyOpen
            );

            closeIcon?.classList.toggle(
                "hidden",
                isCurrentlyOpen
            );

            menuButton.setAttribute(
                "aria-expanded",
                String(!isCurrentlyOpen)
            );

            menuButton.setAttribute(
                "aria-label",
                isCurrentlyOpen
                    ? "Open navigation menu"
                    : "Close navigation menu"
            );
        });


        /*
        |--------------------------------------------------------------------------
        | CLOSE MOBILE MENU AFTER CLICKING A LINK
        |--------------------------------------------------------------------------
        */

        const mobileLinks =
            mobileMenu.querySelectorAll("a");

        mobileLinks.forEach((link) => {

            link.addEventListener("click", () => {

                mobileMenu.classList.add("hidden");

                openIcon?.classList.remove("hidden");

                closeIcon?.classList.add("hidden");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

                menuButton.setAttribute(
                    "aria-label",
                    "Open navigation menu"
                );
            });

        });


        /*
        |--------------------------------------------------------------------------
        | CLOSE MOBILE MENU WITH ESCAPE
        |--------------------------------------------------------------------------
        */

        document.addEventListener("keydown", (event) => {

            if (
                event.key === "Escape" &&
                !mobileMenu.classList.contains("hidden")
            ) {

                mobileMenu.classList.add("hidden");

                openIcon?.classList.remove("hidden");

                closeIcon?.classList.add("hidden");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

                menuButton.setAttribute(
                    "aria-label",
                    "Open navigation menu"
                );
            }

        });

    }


    /*
    |--------------------------------------------------------------------------
    | HEADER SCROLL EFFECT
    |--------------------------------------------------------------------------
    */

    if (header) {

        const updateHeader = () => {

            if (window.scrollY > 20) {

                header.classList.add(
                    "bg-[#05070D]/98",
                    "shadow-2xl",
                    "shadow-black/20"
                );

            } else {

                header.classList.remove(
                    "bg-[#05070D]/98",
                    "shadow-2xl",
                    "shadow-black/20"
                );

            }

        };


        updateHeader();

        window.addEventListener(
            "scroll",
            updateHeader,
            { passive: true }
        );

    }


    /*
    |--------------------------------------------------------------------------
    | SMOOTH INTERNAL SCROLLING
    |--------------------------------------------------------------------------
    */

    const internalLinks =
        document.querySelectorAll('a[href^="#"]');

    internalLinks.forEach((link) => {

        link.addEventListener("click", (event) => {

            const targetId =
                link.getAttribute("href");

            if (
                !targetId ||
                targetId === "#"
            ) {
                return;
            }

            const target =
                document.querySelector(targetId);

            if (!target) {
                return;
            }

            event.preventDefault();

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        });

    });

});