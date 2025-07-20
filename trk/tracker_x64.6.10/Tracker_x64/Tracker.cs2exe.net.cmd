
@rem -Begin-------------------------------------------------------------
@rem
@rem  Install dotNET SDK and set DOTNET_ROOT environment variable.
@rem  Depending on which release is used, the comments in the code
@rem  below are to be moved. Standard is dotNET 8.
@rem
@rem -------------------------------------------------------------------

mkdir Tracker_RunScript

copy Tracker_RunScript.cs Tracker_RunScript\Tracker_RunScript.cs
@rem copy Tracker.RunScript.net6.csproj Tracker_RunScript\Tracker_RunScript.csproj
copy Tracker.RunScript.net8.csproj Tracker_RunScript\Tracker_RunScript.csproj

@cd Tracker_RunScript

dotnet build

@rem start /w /min bin\Debug\net6.0\Tracker_RunScript.exe
start /w /min bin\Debug\net8.0\Tracker_RunScript.exe

@cd..

rmdir /s /q Tracker_RunScript

@rem -End---------------------------------------------------------------
