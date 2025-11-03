#!/usr/bin/env python3
"""
Central AI V2 - Advanced AI Assistant
Main Entry Point
Created by: XdpzQ
"""

import os
import sys
from colorama import init, Fore, Style
from core.brain import Brain
from config import config

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display awesome banner"""
    banner = f"""
{Fore.RED}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        {Fore.LIGHTRED_EX}█▀▀ █▀▀ █▄░█ ▀█▀ █▀█ ▄▀█ █░░   ▄▀█ █{Fore.RED}         ║
║        {Fore.LIGHTRED_EX}█▄▄ ██▄ █░▀█ ░█░ █▀▄ █▀█ █▄▄   █▀█ █{Fore.RED}         ║
║                                                           ║
║            {Fore.WHITE}Advanced AI Assistant System{Fore.RED}                  ║
║                                                           ║
║  {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RED}  ║
║                                                           ║
║  {Fore.WHITE}Version    : {Fore.GREEN}{config.VERSION}{Fore.RED}                                      ║
║  {Fore.WHITE}Status     : {Fore.GREEN}● ONLINE{Fore.RED}                                  ║
║  {Fore.WHITE}Model      : {Fore.YELLOW}Worm 2.0 Flash{Fore.RED}                         ║
║  {Fore.WHITE}Creator    : {Fore.MAGENTA}XdpzQ{Fore.RED}                                      ║
║  {Fore.WHITE}Memory     : {Fore.GREEN}ACTIVE{Fore.RED}                                    ║
║                                                           ║
║  {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RED}  ║
║                                                           ║
║  {Fore.YELLOW}Powerful • Ethical • Professional • Reliable{Fore.RED}         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def print_help():
    """Display help menu"""
    help_text = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════╗
║                    HELP MENU                         ║
╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}[BASIC COMMANDS]{Style.RESET_ALL}
  • Just type your question/request normally
  • AI will understand and help you

{Fore.YELLOW}[SPECIAL COMMANDS]{Style.RESET_ALL}
  {Fore.GREEN}help{Style.RESET_ALL}      - Show this help menu
  {Fore.GREEN}clear{Style.RESET_ALL}     - Clear the screen
  {Fore.GREEN}info{Style.RESET_ALL}      - Show session information
  {Fore.GREEN}memory{Style.RESET_ALL}    - Show memory statistics
  {Fore.GREEN}reset{Style.RESET_ALL}     - Reset conversation history
  {Fore.GREEN}exit{Style.RESET_ALL}      - Exit Central AI (also: quit, bye, keluar)

{Fore.YELLOW}[CAPABILITIES]{Style.RESET_ALL}
  • Programming & Development (Python, JS, PHP, etc)
  • Ethical Hacking & Security Analysis
  • OSINT & Information Gathering
  • Data Science & Machine Learning
  • System Administration & DevOps
  • Automation & Scripting

{Fore.YELLOW}[TIPS]{Style.RESET_ALL}
  • Be specific with your questions
  • Ask for code examples if needed
  • Request explanations for complex topics
  • Use proper context for better responses

{Fore.CYAN}═══════════════════════════════════════════════════════{Style.RESET_ALL}
"""
    print(help_text)

def print_session_info(brain):
    """Display session information"""
    info = brain.memory.get_session_info()
    duration = str(info['duration']).split('.')[0]
    
    info_text = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════╗
║                SESSION INFORMATION                   ║
╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}Session Details:{Style.RESET_ALL}
  • Start Time       : {info['session_start'].strftime('%Y-%m-%d %H:%M:%S')}
  • Duration         : {duration}
  • Total Interactions : {info['total_interactions']}

{Fore.YELLOW}Memory Status:{Style.RESET_ALL}
  • Short-term Items : {info['short_term_items']}/{config.SHORT_TERM_MEMORY_SIZE}
  • Long-term Items  : {info['long_term_items']}/{config.LONG_TERM_MEMORY_SIZE}

{Fore.YELLOW}API Status:{Style.RESET_ALL}
  • Current Key Index: {brain.current_key_index}
  • Total Keys       : {len(config.GEMINI_API_KEYS)}

{Fore.CYAN}═══════════════════════════════════════════════════════{Style.RESET_ALL}
"""
    print(info_text)

def main():
    """Main application loop"""
    clear_screen()
    print_banner()
    
    # Initialize AI Brain
    try:
        brain = Brain()
        print(f"{Fore.GREEN}[✓]{Style.RESET_ALL} AI System initialized successfully!")
        print(f"{Fore.GREEN}[✓]{Style.RESET_ALL} Memory system ready!")
        print(f"{Fore.GREEN}[✓]{Style.RESET_ALL} API connection established!\n")
    except Exception as e:
        print(f"{Fore.RED}[✗]{Style.RESET_ALL} Failed to initialize AI: {str(e)}")
        return
    
    print(f"{Fore.YELLOW}[TIP]{Style.RESET_ALL} Ketik '{Fore.CYAN}help{Style.RESET_ALL}' untuk melihat commands yang tersedia")
    print(f"{Fore.YELLOW}[TIP]{Style.RESET_ALL} Mulai chat dengan mengetik pertanyaan atau permintaan\n")
    print(f"{Fore.CYAN}{'═' * 60}{Style.RESET_ALL}\n")
    
    # Welcome message
    print(f"{Fore.RED}Central AI >{Style.RESET_ALL} Halo bro! Welcome to Central AI V2.")
    print(f"{Fore.RED}Central AI >{Style.RESET_ALL} Gw siap bantu lo dengan berbagai task. Tanya aja!\n")
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Fore.LIGHTBLUE_EX}You >{Style.RESET_ALL} ").strip()
            
            if not user_input:
                continue
            
            # Check for special commands
            if user_input.lower() in ['exit', 'quit', 'bye', 'keluar']:
                print(f"\n{Fore.RED}[SYSTEM]{Style.RESET_ALL} Shutting down Central AI V2...")
                print(f"{Fore.GREEN}Terima kasih sudah menggunakan Central AI! Sampai jumpa! 👋{Style.RESET_ALL}\n")
                break
            
            elif user_input.lower() == 'clear':
                clear_screen()
                print_banner()
                continue
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'info':
                print_session_info(brain)
                continue
            
            elif user_input.lower() == 'memory':
                context = brain.memory.get_context()
                if context:
                    print(f"\n{Fore.CYAN}[MEMORY CONTEXT]{Style.RESET_ALL}")
                    print(f"{context}\n")
                else:
                    print(f"\n{Fore.YELLOW}[INFO]{Style.RESET_ALL} Memory is empty\n")
                continue
            
            elif user_input.lower() == 'reset':
                brain.clear_conversation()
                print(f"\n{Fore.GREEN}[✓]{Style.RESET_ALL} Conversation history has been reset!\n")
                continue
            
            # Process with AI
            print(f"{Fore.YELLOW}[AI]{Style.RESET_ALL} Processing...", end='\r')
            response = brain.process_input(user_input)
            print(" " * 50, end='\r')  # Clear "Processing..." message
            
            # Display response with formatting
            print(f"{Fore.RED}Central AI >{Style.RESET_ALL} {response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}[SYSTEM]{Style.RESET_ALL} Interrupted by user")
            print(f"{Fore.GREEN}Terima kasih sudah menggunakan Central AI! Sampai jumpa! 👋{Style.RESET_ALL}\n")
            break
            
        except Exception as e:
            print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} Terjadi kesalahan: {str(e)}\n")
            if config.DEBUG_MODE:
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{Fore.RED}[FATAL ERROR]{Style.RESET_ALL} {str(e)}")
        sys.exit(1)
