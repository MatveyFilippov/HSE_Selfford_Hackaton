package com.kis.cat.hacminin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import by.kirich1409.viewbindingdelegate.viewBinding
import com.kis.cat.hacminin.databinding.ActivityMainBinding
import com.kis.cat.hacminin.ui.BotomActivity

class MainActivity : AppCompatActivity(R.layout.activity_main) {

    private val binding: ActivityMainBinding by viewBinding()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        Handler(Looper.getMainLooper()).postDelayed(Runnable {
                startActivity(Intent(this, BotomActivity::class.java))
        }, 3000)
    }
}