/**
 * ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 * ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
 * ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 * ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 * ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 * ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
 * Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
 */
/**
 * Animated ASCII Art Page Scripts
 * Document-specific JavaScript for animated-ascii-art.md
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';
    
    // Check if PhantomASCII is available
    if (typeof PhantomASCII === 'undefined') {
        console.error('PhantomASCII module not loaded');
        return;
    }
    
    // Initialize PhantomASCII for pulse demo
    const pulseDemo = document.getElementById('phantom-ascii-pulse');
    if (pulseDemo) {
        const phantomAnimation = new PhantomASCII('phantom-ascii-pulse', {
            animationSpeed: 500,
            onStart: function() {
                const btn = document.getElementById('pulse-toggle-btn');
                if (btn) {
                    btn.innerHTML = '<i class="fas fa-pause"></i> Pause';
                }
            },
            onStop: function() {
                const btn = document.getElementById('pulse-toggle-btn');
                if (btn) {
                    btn.innerHTML = '<i class="fas fa-play"></i> Play';
                }
            },
            onError: function(message) {
                const alertBox = document.getElementById('pulse-error-alert');
                const errorMsg = document.getElementById('pulse-error-message');
                if (alertBox && errorMsg) {
                    errorMsg.textContent = message || 'An unexpected error occurred';
                    alertBox.style.display = 'block';
                }
            }
        });

        // Button click handler
        const toggleBtn = document.getElementById('pulse-toggle-btn');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', function() {
                phantomAnimation.toggle();
            });
        }
    }

    // Initialize PhantomASCII for error test demo
    const testDemo = document.getElementById('phantom-ascii-test');
    if (testDemo) {
        window.testAnimation = new PhantomASCII('phantom-ascii-test', {
            animationSpeed: 500,
            onError: function(message) {
                const alertBox = document.getElementById('test-error-alert');
                const errorMsg = document.getElementById('test-error-message');
                if (alertBox && errorMsg) {
                    errorMsg.textContent = message || 'An unexpected error occurred';
                    alertBox.style.display = 'block';
                }
            }
        });

        // Test error button handler
        const errorBtn = document.getElementById('test-error-btn');
        if (errorBtn) {
            errorBtn.addEventListener('click', function() {
                if (window.testAnimation) {
                    window.testAnimation.setError('Connection failed');
                }
            });
        }

        // Clear error button handler
        const clearBtn = document.getElementById('clear-error-btn');
        if (clearBtn) {
            clearBtn.addEventListener('click', function() {
                if (window.testAnimation) {
                    window.testAnimation.clearError();
                    // Hide the error alert box
                    const alertBox = document.getElementById('test-error-alert');
                    if (alertBox) {
                        alertBox.style.display = 'none';
                    }
                }
            });
        }
    }

    // Initialize PhantomASCII for speed control demo
    const speedDemo = document.getElementById('phantom-ascii-speed');
    if (speedDemo) {
        const speedAnimation = new PhantomASCII('phantom-ascii-speed', {
            animationSpeed: 500,
            autoStart: false,  // Start in stopped state
            onStart: function() {
                const btn = document.getElementById('speed-toggle-btn');
                if (btn) {
                    btn.innerHTML = '<i class="fas fa-pause"></i> Pause';
                }
            },
            onStop: function() {
                const btn = document.getElementById('speed-toggle-btn');
                if (btn) {
                    btn.innerHTML = '<i class="fas fa-play"></i> Play';
                }
            }
        });

        // Speed slider control
        const speedSlider = document.getElementById('speed-slider');
        const speedValue = document.getElementById('speed-value');
        
        if (speedSlider && speedValue) {
            // Handle slider input
            speedSlider.addEventListener('input', function(e) {
                const speed = parseInt(e.target.value);
                speedValue.textContent = speed.toString();
                speedAnimation.setSpeed(speed);
            });

            // Handle range change (for better browser support)
            speedSlider.addEventListener('change', function(e) {
                const speed = parseInt(e.target.value);
                speedValue.textContent = speed.toString();
                speedAnimation.setSpeed(speed);
            });
        }

        // Speed toggle button
        const speedToggleBtn = document.getElementById('speed-toggle-btn');
        if (speedToggleBtn) {
            speedToggleBtn.addEventListener('click', function() {
                speedAnimation.toggle();
            });
        }
    }
});